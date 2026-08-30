#!/usr/bin/env python3
"""Emit raw ChatGPT-export messages as JSON Lines using only the standard library."""

import argparse
import json
import sys
from pathlib import Path


def text_from_content(content):
    if not isinstance(content, dict):
        return ""
    parts = content.get("parts")
    if isinstance(parts, list):
        return "\n".join(part for part in parts if isinstance(part, str))
    text = content.get("text")
    return text if isinstance(text, str) else ""


def conversations(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and isinstance(payload.get("conversations"), list):
        return payload["conversations"]
    if isinstance(payload, dict) and isinstance(payload.get("mapping"), dict):
        return [payload]
    raise ValueError("expected a ChatGPT export array or a conversation object with mapping")


def emit(conversation, exclude_system, output):
    mapping = conversation.get("mapping", {})
    if not isinstance(mapping, dict):
        return 0
    rows = []
    for node_id, node in mapping.items():
        if not isinstance(node, dict) or not isinstance(node.get("message"), dict):
            continue
        message = node["message"]
        author = message.get("author") if isinstance(message.get("author"), dict) else {}
        role = author.get("role")
        if exclude_system and role == "system":
            continue
        content = text_from_content(message.get("content"))
        rows.append((message.get("create_time") or 0, {
            "conversation_id": conversation.get("conversation_id") or conversation.get("id"),
            "title": conversation.get("title"),
            "conversation_create_time": conversation.get("create_time"),
            "message_id": message.get("id") or node_id,
            "parent_id": node.get("parent"),
            "message_create_time": message.get("create_time"),
            "role": role,
            "content": content,
            "raw_message": message,
            "raw_node": node,
        }))
    for _, row in sorted(rows, key=lambda item: item[0]):
        output.write(json.dumps(row, ensure_ascii=False) + "\n")
    return len(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="ChatGPT export JSON path, or - for stdin")
    parser.add_argument("--output", "-o", help="JSONL output path; default: stdout")
    parser.add_argument("--exclude-system", action="store_true")
    parser.add_argument("--include-system", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()

    source = sys.stdin if args.input == "-" else Path(args.input).open(encoding="utf-8")
    try:
        payload = json.load(source)
    finally:
        if source is not sys.stdin:
            source.close()
    destination = sys.stdout if not args.output else Path(args.output).open("w", encoding="utf-8")
    try:
        count = sum(emit(item, args.exclude_system, destination) for item in conversations(payload))
    finally:
        if destination is not sys.stdout:
            destination.close()
    print("normalized {} raw messages".format(count), file=sys.stderr)


if __name__ == "__main__":
    main()
