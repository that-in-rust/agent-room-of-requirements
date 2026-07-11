import argparse
import csv
import json
import os
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from tests.test_idiomatic_reference_evolution import (  # noqa: E402
    QUEUE_PATH,
    load_csv_dictionary_rows,
    resolve_packet_output_path,
)
from tests.verify_idiomatic_reference_file import (  # noqa: E402
    load_reference_owner_identifier,
    validate_question_packet_artifact,
    validate_reference_file_artifact,
)


def verify_reference_before_update(relative_path):
    working_path = (REPO_ROOT / relative_path).resolve()
    working_path.relative_to(REPO_ROOT)
    owner = load_reference_owner_identifier(relative_path)
    packet_path = resolve_packet_output_path(owner, working_path)
    reference_result = validate_reference_file_artifact(working_path)
    packet_result = validate_question_packet_artifact(packet_path)
    return {
        "owner": owner,
        "packetPath": packet_path,
        "reference": reference_result,
        "packet": packet_result,
    }


def mark_verified_reference_complete(queue_rows, relative_path, verification):
    packet_relative = verification["packetPath"].relative_to(REPO_ROOT).as_posix()
    updated_rows = 0
    for row in queue_rows:
        if row["reference_file_path"] != relative_path:
            continue
        section_order = int(row["section_order"])
        row["task_status"] = "complete"
        row["completion_notes"] = (
            f"packet={packet_relative}; section={section_order:03d}; "
            "ten_questions=complete; block=evolved; "
            "section_reconciliation=complete; file_reread=complete"
        )
        updated_rows += 1
    if updated_rows == 0:
        raise AssertionError(f"queue contains no rows for {relative_path}")
    return updated_rows


def mark_reference_rows_pending(queue_rows, relative_path):
    updated_rows = 0
    for row in queue_rows:
        if row["reference_file_path"] != relative_path:
            continue
        row["task_status"] = "pending"
        row["completion_notes"] = ""
        updated_rows += 1
    if updated_rows == 0:
        raise AssertionError(f"queue contains no rows for {relative_path}")
    return updated_rows


def write_queue_dictionary_rows(queue_rows):
    if not queue_rows:
        raise AssertionError("cannot write an empty queue")
    fieldnames = list(queue_rows[0])
    temporary_path = QUEUE_PATH.with_suffix(".csv.tmp")
    with temporary_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(queue_rows)
        handle.flush()
        os.fsync(handle.fileno())
    temporary_path.replace(QUEUE_PATH)


def main_update_queue_status():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", action="append", required=True)
    parser.add_argument("--reopen", action="store_true")
    arguments = parser.parse_args()

    queue_rows = load_csv_dictionary_rows(QUEUE_PATH)
    results = []
    for relative_path in arguments.path:
        if arguments.reopen:
            updated_rows = mark_reference_rows_pending(queue_rows, relative_path)
            results.append({
                "referencePath": relative_path,
                "updatedRows": updated_rows,
                "status": "pending",
            })
            continue

        verification = verify_reference_before_update(relative_path)
        updated_rows = mark_verified_reference_complete(
            queue_rows,
            relative_path,
            verification,
        )
        results.append({
            "referencePath": relative_path,
            "owner": verification["owner"],
            "updatedRows": updated_rows,
            "sections": verification["reference"]["sectionCount"],
            "questions": verification["packet"]["questionCount"],
            "fields": verification["packet"]["fieldCount"],
        })

    write_queue_dictionary_rows(queue_rows)
    print(json.dumps({"status": "PASS", "updated": results}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main_update_queue_status()
