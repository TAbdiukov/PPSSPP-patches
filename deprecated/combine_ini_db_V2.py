#!/usr/bin/env python3
"""Combine prefixed .ini.db fragments by their original filename.

Usage: python combine_ini_db_V2.py [folder]

The folder is scanned non-recursively. Inputs use
"<category>_<name>.ini.db" and outputs are named "<name>.ini.db" in the
same folder. Generated combined files are ignored on later runs.
"""

import argparse
import re
from pathlib import Path

GAME = re.compile(r"^_S\s+(\S+)\s*$")
TITLE = re.compile(r"^_G\s+(.+?)\s*$")
EMBEDDED_GAME = re.compile(r"_S\s+[A-Za-z0-9-]+\s*$")
SECTION = re.compile(r"^_C0\s+_+\[>>.+<<\]_+\s*$", re.MULTILINE)


def parse_file(path):
    lines = []
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        match = EMBEDDED_GAME.search(line)
        if match and match.start() > 0:
            lines.extend((line[: match.start()], line[match.start() :]))
        else:
            lines.append(line)

    blocks = []
    preamble = []
    game_id = title = None
    body = []

    def finish():
        if game_id is None:
            return
        while body and not body[0].strip():
            body.pop(0)
        while body and not body[-1].strip():
            body.pop()
        blocks.append((game_id, title, body.copy()))

    for line in lines:
        match = GAME.match(line)
        if match:
            finish()
            game_id = match.group(1)
            title = None
            body = preamble
            preamble = []
            continue

        if game_id is None:
            preamble.append(line)
            continue

        match = TITLE.match(line)
        if match and title is None:
            title = match.group(1)
        else:
            body.append(line)

    finish()
    return blocks


def category_order(category):
    category = category.casefold()
    if category == "cheats":
        return (2, "")
    if category == "debug":
        return (1, "")
    return (0, category)


def combine(folder):
    outputs = {}

    for path in sorted(folder.glob("*.ini.db"), key=lambda p: p.name.casefold()):
        stem = path.name[: -len(".ini.db")]
        if "_" not in stem:
            continue

        text = path.read_text(encoding="utf-8-sig")
        if SECTION.search(text):
            continue

        category, output_stem = stem.split("_", 1)
        blocks = parse_file(path)
        if not blocks:
            continue

        games = outputs.setdefault(output_stem, {})
        for game_id, title, body in blocks:
            if game_id not in games:
                games[game_id] = {"title": title or game_id, "categories": {}}
            elif games[game_id]["title"] == game_id and title:
                games[game_id]["title"] = title

            sections = games[game_id]["categories"]
            sections.setdefault(category, []).append(body)

    written = []
    for output_stem in sorted(outputs, key=str.casefold):
        output = []

        for game_id, game in outputs[output_stem].items():
            if output:
                output.append("")

            output.extend((f"_S {game_id}", f"_G {game['title']}", "//"))

            for category in sorted(game["categories"], key=category_order):
                label = category.replace("-", " ").title()
                output.extend((f"_C0 _________[>>{label}<<]_________", "//"))

                for body in game["categories"][category]:
                    output.extend(body)
                    if output[-1] != "//":
                        output.append("//")

        destination = folder / f"{output_stem}.ini.db"
        destination.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")
        written.append(destination)

    return written


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Combine prefixed .ini.db files and remove the category prefix "
            "from each output filename."
        )
    )
    parser.add_argument(
        "folder",
        nargs="?",
        type=Path,
        default=Path.cwd(),
        help="folder to scan (default: current folder)",
    )
    args = parser.parse_args()

    for path in combine(args.folder):
        print(path.name)


if __name__ == "__main__":
    main()
