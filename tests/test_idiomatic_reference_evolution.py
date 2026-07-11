import csv
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKING_DIRECTORY = REPO_ROOT / "idiomatic-ref-202607"
ARCHIVE_DIRECTORY = (
    REPO_ROOT
    / "agents-used-monthly-archive"
    / "idiomatic-references-202606"
    / "generated-references"
)
QUEUE_PATH = REPO_ROOT / "idiomatic-reference-evolution-tasks-202607.csv"
SPEC_PATH = REPO_ROOT / "idiomatic-reference-evolution-spec-202607.md"
WORK_DIRECTORY = REPO_ROOT / "idiomatic-reference-evolution-work"
AGENT_LANES = {
    "evolve_reference_sections_alpha": "alpha",
    "evolve_reference_sections_beta": "beta",
    "evolve_reference_sections_gamma": "gamma",
    "evolve_reference_sections_delta": "delta",
}
PACKET_FIELDS = (
    "current_section_observation",
    "supporting_reason",
    "counterargument_or_limit",
    "assumptions_and_boundaries",
    "revision_decision",
    "additional_insight_to_add",
)
PACKET_CONTEXT_PREFIX_PATTERN = re.compile(
    r'^Section \d{3}\s+(?:\([^)]*\)|"[^"]*"),\s*'
    r'Question \d{2}(?:\s+on\s+[^:]+)?:?\s*'
)


def load_csv_dictionary_rows(csv_path):
    with csv_path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def resolve_archive_source_path(working_path):
    archive_name = re.sub(r"-20260710\.md$", ".md", working_path.name)
    return ARCHIVE_DIRECTORY / archive_name


def parse_markdown_heading_sections(markdown_text):
    lines = markdown_text.splitlines()
    headings = []
    active_fence = None

    for line_number, line in enumerate(lines, start=1):
        fence_match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence_match:
            marker = fence_match.group(1)[0]
            marker_length = len(fence_match.group(1))
            if active_fence is None:
                active_fence = (marker, marker_length)
            elif active_fence[0] == marker and marker_length >= active_fence[1]:
                active_fence = None
            continue
        if active_fence is not None:
            continue
        heading_match = re.match(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$", line)
        if heading_match:
            headings.append((line_number, heading_match.group(2).strip()))

    sections = []
    for index, (start_line, heading_text) in enumerate(headings):
        end_line = headings[index + 1][0] - 1 if index + 1 < len(headings) else len(lines)
        section_text = "\n".join(lines[start_line - 1 : end_line])
        sections.append((heading_text, section_text))
    return sections


def load_specification_question_texts():
    specification = SPEC_PATH.read_text(encoding="utf-8")
    question_block = specification.split("### Ten Section Questions", 1)[1]
    question_block = question_block.split("### Mandatory Question Packet", 1)[0]
    return [
        match.group(1).strip()
        for match in re.finditer(r"^\d+\. (.+)$", question_block, flags=re.MULTILINE)
    ]


def resolve_packet_output_path(agent_id, working_path):
    lane = AGENT_LANES[agent_id]
    packet_name = f"{working_path.stem}-question-packets.md"
    return WORK_DIRECTORY / lane / "packets" / packet_name


def normalize_packet_field_content(field_value):
    without_context_prefix = PACKET_CONTEXT_PREFIX_PATTERN.sub("", field_value.strip())
    return re.sub(r"\s+", " ", without_context_prefix).casefold()


class IdiomaticReferenceEvolutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.queue_rows = load_csv_dictionary_rows(QUEUE_PATH)
        cls.working_paths = sorted(WORKING_DIRECTORY.glob("*-20260710.md"))
        cls.owner_by_path = {}
        for row in cls.queue_rows:
            relative_path = row["reference_file_path"]
            cls.owner_by_path.setdefault(relative_path, set()).add(row["agent_id"])

    def test_inventory_matches_specification(self):
        self.assertEqual(len(self.working_paths), 99)
        self.assertEqual(len(self.queue_rows), 11961)
        self.assertEqual(len(self.owner_by_path), 99)

    def test_owner_mapping_unique(self):
        self.assertEqual(set(AGENT_LANES), {
            owner
            for owners in self.owner_by_path.values()
            for owner in owners
        })
        for relative_path, owners in self.owner_by_path.items():
            self.assertEqual(owners, {next(iter(owners))}, relative_path)

    def test_assignment_manifests_match(self):
        expected_by_lane = {lane: set() for lane in AGENT_LANES.values()}
        for row in self.queue_rows:
            lane = AGENT_LANES[row["agent_id"]]
            expected_by_lane[lane].add(
                (int(row["agent_file_order"]), row["reference_file_path"])
            )

        for lane, expected in expected_by_lane.items():
            manifest_path = WORK_DIRECTORY / lane / "assignments.csv"
            manifest_rows = load_csv_dictionary_rows(manifest_path)
            actual = {
                (int(row["agent_file_order"]), row["reference_file_path"])
                for row in manifest_rows
            }
            self.assertEqual(actual, expected, lane)

    def test_reference_files_evolved(self):
        unchanged_files = []
        unexpanded_sections = []

        for working_path in self.working_paths:
            archive_path = resolve_archive_source_path(working_path)
            working_text = working_path.read_text(encoding="utf-8")
            archive_text = archive_path.read_text(encoding="utf-8")
            if working_text == archive_text:
                unchanged_files.append(working_path.name)

            working_sections = parse_markdown_heading_sections(working_text)
            archive_sections = parse_markdown_heading_sections(archive_text)
            self.assertEqual(
                [heading for heading, _ in working_sections],
                [heading for heading, _ in archive_sections],
                working_path.name,
            )
            self.assertEqual(len(working_sections), len(archive_sections), working_path.name)
            for section_order, ((heading, working_section), (_, archive_section)) in enumerate(
                zip(working_sections, archive_sections),
                start=1,
            ):
                if len(working_section.strip()) <= len(archive_section.strip()):
                    unexpanded_sections.append(
                        f"{working_path.name}:section-{section_order:03d}:{heading}"
                    )

        self.assertEqual(unchanged_files, [], f"unchanged files: {unchanged_files[:10]}")
        self.assertEqual(
            unexpanded_sections,
            [],
            f"sections not expanded: {unexpanded_sections[:20]}",
        )

    def test_question_packets_complete(self):
        expected_questions = load_specification_question_texts()
        self.assertEqual(len(expected_questions), 10)
        missing_packets = []
        malformed_packets = []

        for working_path in self.working_paths:
            relative_path = working_path.relative_to(REPO_ROOT).as_posix()
            owner = next(iter(self.owner_by_path[relative_path]))
            packet_path = resolve_packet_output_path(owner, working_path)
            if not packet_path.exists():
                missing_packets.append(packet_path.relative_to(REPO_ROOT).as_posix())
                continue

            packet_text = packet_path.read_text(encoding="utf-8")
            packet_field_values = []
            section_chunks = re.split(r"(?=^## Section \d{3}:)", packet_text, flags=re.MULTILINE)
            section_chunks = [chunk for chunk in section_chunks if chunk.startswith("## Section ")]
            if len(section_chunks) != 26:
                malformed_packets.append(f"{packet_path.name}:sections={len(section_chunks)}")
                continue

            for section_order, section_chunk in enumerate(section_chunks, start=1):
                question_chunks = re.split(
                    r"(?=^### Question \d{2}:)",
                    section_chunk,
                    flags=re.MULTILINE,
                )
                question_chunks = [
                    chunk for chunk in question_chunks if chunk.startswith("### Question ")
                ]
                if len(question_chunks) != 10:
                    malformed_packets.append(
                        f"{packet_path.name}:section-{section_order:03d}:questions={len(question_chunks)}"
                    )
                    continue

                self.assertEqual(len(question_chunks), len(expected_questions), packet_path.name)
                for question_order, (question_chunk, expected_question) in enumerate(
                    zip(question_chunks, expected_questions),
                    start=1,
                ):
                    heading_line = question_chunk.splitlines()[0]
                    actual_question = heading_line.split(":", 1)[1].strip()
                    if actual_question != expected_question:
                        malformed_packets.append(
                            f"{packet_path.name}:section-{section_order:03d}:question-{question_order:02d}:text"
                        )
                    for field_name in PACKET_FIELDS:
                        field_match = re.search(
                            rf"^[-*] \*\*{re.escape(field_name)}:\*\*\s+(.+)$",
                            question_chunk,
                            flags=re.MULTILINE,
                        )
                        if not field_match or not field_match.group(1).strip():
                            malformed_packets.append(
                                f"{packet_path.name}:section-{section_order:03d}:question-{question_order:02d}:{field_name}"
                            )
                        else:
                            packet_field_values.append(field_match.group(1).strip())

            duplicate_field_count = len(packet_field_values) - len(set(packet_field_values))
            if duplicate_field_count:
                malformed_packets.append(
                    f"{packet_path.name}:duplicate_field_values={duplicate_field_count}"
                )

            normalized_field_values = [
                normalize_packet_field_content(field_value)
                for field_value in packet_field_values
            ]
            normalized_duplicate_count = len(normalized_field_values) - len(
                set(normalized_field_values)
            )
            if normalized_duplicate_count:
                malformed_packets.append(
                    f"{packet_path.name}:normalized_duplicate_field_values="
                    f"{normalized_duplicate_count}"
                )

        self.assertEqual(missing_packets, [], f"missing packets: {missing_packets[:10]}")
        self.assertEqual(malformed_packets, [], f"malformed packets: {malformed_packets[:20]}")

    def test_packet_content_uniqueness(self):
        offending_packets = []
        field_line_pattern = re.compile(
            r"^[-*] \*\*[^*]+:\*\*\s+(.+)$",
            flags=re.MULTILINE,
        )

        for packet_path in WORK_DIRECTORY.glob("*/packets/*.md"):
            packet_text = packet_path.read_text(encoding="utf-8")
            field_values = [
                match.group(1).strip()
                for match in field_line_pattern.finditer(packet_text)
            ]
            if len(field_values) != 26 * 10 * len(PACKET_FIELDS):
                continue

            normalized_field_values = [
                normalize_packet_field_content(field_value)
                for field_value in field_values
            ]
            normalized_duplicate_count = len(normalized_field_values) - len(
                set(normalized_field_values)
            )
            if normalized_duplicate_count:
                offending_packets.append(
                    f"{packet_path.name}:{normalized_duplicate_count}"
                )

        self.assertEqual(
            offending_packets,
            [],
            f"normalized duplicate packet fields: {offending_packets}",
        )

    def test_queue_rows_complete(self):
        incomplete_rows = [
            row["unit_id"]
            for row in self.queue_rows
            if row["task_status"] != "complete" or not row["completion_notes"].strip()
        ]
        self.assertEqual(incomplete_rows, [], f"incomplete rows: {incomplete_rows[:20]}")

    def test_reference_placeholders_absent(self):
        placeholder_pattern = re.compile(r"\b(?:TODO|TBD|FIXME|STUB)\b")
        offending_paths = []
        candidate_paths = list(self.working_paths)
        candidate_paths.extend(WORK_DIRECTORY.glob("*/packets/*.md"))
        for candidate_path in candidate_paths:
            if placeholder_pattern.search(candidate_path.read_text(encoding="utf-8")):
                offending_paths.append(candidate_path.relative_to(REPO_ROOT).as_posix())
        self.assertEqual(offending_paths, [], f"placeholder files: {offending_paths[:20]}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
