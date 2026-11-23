import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tests.test_idiomatic_reference_evolution import (
    PACKET_FIELDS,
    QUEUE_PATH,
    REPO_ROOT,
    load_csv_dictionary_rows,
    load_specification_question_texts,
    normalize_packet_field_content,
    parse_markdown_heading_sections,
    resolve_archive_source_path,
    resolve_packet_output_path,
)


def load_reference_owner_identifier(relative_path):
    owners = {
        row["agent_id"]
        for row in load_csv_dictionary_rows(QUEUE_PATH)
        if row["reference_file_path"] == relative_path
    }
    if len(owners) != 1:
        raise AssertionError(f"expected one owner for {relative_path}, found {sorted(owners)}")
    return next(iter(owners))


def validate_reference_file_artifact(working_path):
    archive_path = resolve_archive_source_path(working_path)
    working_text = working_path.read_text(encoding="utf-8")
    archive_text = archive_path.read_text(encoding="utf-8")
    if working_text == archive_text:
        raise AssertionError("working reference still matches archive seed")

    working_sections = parse_markdown_heading_sections(working_text)
    archive_sections = parse_markdown_heading_sections(archive_text)
    working_headings = [heading for heading, _ in working_sections]
    archive_headings = [heading for heading, _ in archive_sections]
    if working_headings != archive_headings:
        raise AssertionError("working headings differ from archive headings")

    unexpanded_sections = []
    for section_order, ((heading, working_section), (_, archive_section)) in enumerate(
        zip(working_sections, archive_sections),
        start=1,
    ):
        if len(working_section.strip()) <= len(archive_section.strip()):
            unexpanded_sections.append(f"section-{section_order:03d}:{heading}")
    if unexpanded_sections:
        raise AssertionError(f"sections not expanded: {unexpanded_sections}")

    placeholder_pattern = re.compile(r"\b(?:TODO|TBD|FIXME|STUB)\b")
    if placeholder_pattern.search(working_text):
        raise AssertionError("working reference contains placeholder language")

    return {
        "sectionCount": len(working_sections),
        "seedCharacters": len(archive_text),
        "evolvedCharacters": len(working_text),
    }


def validate_question_packet_artifact(packet_path):
    if not packet_path.exists():
        raise AssertionError(f"missing question packet: {packet_path}")

    packet_text = packet_path.read_text(encoding="utf-8")
    expected_questions = load_specification_question_texts()
    section_chunks = re.split(r"(?=^## Section \d{3}:)", packet_text, flags=re.MULTILINE)
    section_chunks = [chunk for chunk in section_chunks if chunk.startswith("## Section ")]
    if len(section_chunks) != 26:
        raise AssertionError(f"expected 26 packet sections, found {len(section_chunks)}")

    question_count = 0
    field_count = 0
    field_values = []
    for section_order, section_chunk in enumerate(section_chunks, start=1):
        question_chunks = re.split(
            r"(?=^### Question \d{2}:)",
            section_chunk,
            flags=re.MULTILINE,
        )
        question_chunks = [chunk for chunk in question_chunks if chunk.startswith("### Question ")]
        if len(question_chunks) != 10:
            raise AssertionError(
                f"section {section_order:03d} expected 10 questions, found {len(question_chunks)}"
            )

        for question_order, (question_chunk, expected_question) in enumerate(
            zip(question_chunks, expected_questions),
            start=1,
        ):
            question_count += 1
            heading_line = question_chunk.splitlines()[0]
            actual_question = heading_line.split(":", 1)[1].strip()
            if actual_question != expected_question:
                raise AssertionError(
                    f"section {section_order:03d} question {question_order:02d} text mismatch"
                )
            for field_name in PACKET_FIELDS:
                field_match = re.search(
                    rf"^[-*] \*\*{re.escape(field_name)}:\*\*\s+(.+)$",
                    question_chunk,
                    flags=re.MULTILINE,
                )
                if not field_match or not field_match.group(1).strip():
                    raise AssertionError(
                        f"section {section_order:03d} question {question_order:02d} missing {field_name}"
                    )
                field_values.append(field_match.group(1).strip())
                field_count += 1

    duplicate_field_count = len(field_values) - len(set(field_values))
    if duplicate_field_count:
        raise AssertionError(
            f"question packet contains {duplicate_field_count} duplicated field values"
        )

    normalized_field_values = [
        normalize_packet_field_content(field_value)
        for field_value in field_values
    ]
    normalized_duplicate_count = len(normalized_field_values) - len(
        set(normalized_field_values)
    )
    if normalized_duplicate_count:
        raise AssertionError(
            "question packet contains "
            f"{normalized_duplicate_count} normalized duplicated field values"
        )

    placeholder_pattern = re.compile(r"\b(?:TODO|TBD|FIXME|STUB)\b")
    if placeholder_pattern.search(packet_text):
        raise AssertionError("question packet contains placeholder language")

    return {
        "sectionCount": len(section_chunks),
        "questionCount": question_count,
        "fieldCount": field_count,
        "uniqueFieldCount": len(set(field_values)),
        "normalizedUniqueFieldCount": len(set(normalized_field_values)),
        "packetCharacters": len(packet_text),
    }


def main_verify_reference_file():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    arguments = parser.parse_args()

    working_path = (REPO_ROOT / arguments.path).resolve()
    relative_path = working_path.relative_to(REPO_ROOT).as_posix()
    owner = load_reference_owner_identifier(relative_path)
    packet_path = resolve_packet_output_path(owner, working_path)
    result = {
        "status": "PASS",
        "referencePath": relative_path,
        "packetPath": packet_path.relative_to(REPO_ROOT).as_posix(),
        "owner": owner,
        "reference": validate_reference_file_artifact(working_path),
        "packet": validate_question_packet_artifact(packet_path),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main_verify_reference_file()
