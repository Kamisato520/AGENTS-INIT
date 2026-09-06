#!/usr/bin/env python3
"""Insert or refresh the AGENT-INIT managed block in AGENTS.md."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

START_RE = re.compile(r"<!-- AGENT-INIT:START -->")
END = "<!-- AGENT-INIT:END -->"


def load_block(skill_dir: Path) -> str:
    path = skill_dir / "assets" / "astra.md"
    if not path.is_file():
        raise SystemExit(f"template not found: {path}")
    return path.read_text(encoding="utf-8").strip()


def merge(existing: str, block: str) -> str:
    match = START_RE.search(existing)
    if not match:
        base = existing.rstrip()
        return f"{base}\n\n{block}\n" if base else f"{block}\n"

    end_pos = existing.find(END, match.end())
    if end_pos < 0:
        raise SystemExit(
            "found AGENT-INIT start marker without matching end marker; "
            "fix AGENTS.md before retrying"
        )

    end_pos += len(END)
    before = existing[: match.start()].rstrip()
    after = existing[end_pos:].lstrip("\n")

    parts = [part for part in (before, block, after.rstrip()) if part]
    return "\n\n".join(parts) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="AGENTS.md")
    parser.add_argument("--create", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    target = Path(args.file)
    if not target.exists() and not args.create:
        raise SystemExit(
            f"{target} does not exist. Run native Codex /init first, "
            "or use --create when explicitly requested."
        )

    existing = target.read_text(encoding="utf-8") if target.exists() else ""
    skill_dir = Path(__file__).resolve().parent.parent
    updated = merge(existing, load_block(skill_dir))

    if args.dry_run:
        print(updated, end="")
        return

    target.write_text(updated, encoding="utf-8")
    print(f"updated {target} with AGENT-INIT")


if __name__ == "__main__":
    main()
