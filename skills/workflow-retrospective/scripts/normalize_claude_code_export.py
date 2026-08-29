#!/usr/bin/env python3
"""Emit complete Claude Code JSONL transcript records as normalized JSON Lines."""

import argparse
import json
import sys
from pathlib import Path


def transcript_files(source):
    if source == "-":
        return [None]
    path = Path(source)
    if path.is_file():
        return [path]
    if path.is_dir():
        return sorted(path.rglob("*.jsonl"))
    raise ValueError("input must be a JSONL file, a directory, or - for stdin")


def emit_file(path, output):
    stream = sys.stdin if path is None else path.open(encoding="utf-8")
    emitted = 0
    malformed = 0
    try:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                malformed += 1
                continue
            if not isinstance(record, dict):
                malformed += 1
                continue
            output.write(json.dumps({
                "source": "claude-code",
                "transcript_path": None if path is None else str(path),
                "line_number": line_number,
                "session_id": record.get("sessionId"),
                "timestamp": record.get("timestamp"),
                "record_type": record.get("type"),
                "is_sidechain": record.get("isSidechain", False),
                "record": record,
            }, ensure_ascii=False) + "\n")
            emitted += 1
    finally:
        if stream is not sys.stdin:
            stream.close()
    return emitted, malformed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Claude Code JSONL file, transcript directory, or - for stdin")
    parser.add_argument("--output", "-o", help="JSONL output path; default: stdout")
    args = parser.parse_args()

    destination = sys.stdout if not args.output else Path(args.output).open("w", encoding="utf-8")
    try:
        emitted = malformed = files = 0
        for path in transcript_files(args.input):
            count, bad = emit_file(path, destination)
            emitted += count
            malformed += bad
            files += 1
    finally:
        if destination is not sys.stdout:
            destination.close()
    print("normalized {} raw records from {} transcript files ({} malformed lines skipped)".format(
        emitted, files, malformed), file=sys.stderr)


if __name__ == "__main__":
    main()
