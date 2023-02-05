#!/usr/bin/env python3
"""Convert a TiddlyWiki to a vw wiki via tiddlers.json

Usage: tiddlers_to_vw.py < tiddlers.json
"""

import json
import re
import sys

# Regular expressions and substitutions
bullet1_re = re.compile(r"^\* ")
bullet1_repl = r"- "
bullet2_re = re.compile(r"\n\* ")
bullet2_repl = r"\n- "
bad_file_chr_re = re.compile(r"[()\[\]\,\!\?\'\"\\]")
bad_file_chr_repl = r""
link_re = re.compile(r"\[\[([^\]\|]+)\|?([^\]]+)?\]\]")
image_re = re.compile(r"\[img\[([^\]]+)\]\]")
image_repl = r"![Image](\1)"
punctuation_re = re.compile(r"([\.\?\1]) ")
punctuation_repl = r"\1\n"


def title_to_filename(title: str) -> str:
    """Convert an article title to its standard filename"""
    title = title.lower().replace(" ", "_") + ".md"
    title = bad_file_chr_re.sub(bad_file_chr_repl, title)
    return title


def link_repl(match: re.Match[str]) -> str:
    """Replace function for link_re"""
    text = match[1]
    if match[2] is not None:
        title = match[2]
    else:
        title = text
    filename = title_to_filename(title)
    return f"[{text}]({filename})"


def main() -> int:
    """Convert all tiddlers passed in from standard in to markdown files"""
    tiddlers = json.load(sys.stdin)
    for tiddler in tiddlers:
        # Skip non-article tiddlers
        if "text" not in tiddler or not tiddler["text"]:
            continue

        # Convert TiddlyWiki syntax to markdown
        text = tiddler["text"]
        text = text.replace("!!", "##")  # heading
        text = text.replace("//", "*")  # italic
        text = text.replace("''", "**")  # bold
        text = text.replace("``", "`")  # code
        text = punctuation_re.sub(punctuation_repl, text)
        text = bullet1_re.sub(bullet1_repl, text)
        text = bullet2_re.sub(bullet2_repl, text)
        text = link_re.sub(link_repl, text)
        text = image_re.sub(image_repl, text)

        # Generate the markdown file
        title = tiddler["title"]
        filename = title_to_filename(title)
        with open(filename, "w") as file:
            file.write(f"# {title}\n\n")
            file.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
