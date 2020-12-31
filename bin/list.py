#!/usr/bin/env python3

import os

from pathlib import Path

from digital_land_frontend.markdown.content_file import read_content_file

from bin.summary import create_summary


def create_list(pages, directory, **kwargs):
    p = os.path.join(directory, "_list.md")
    f = Path(p)
    data = read_content_file(f, expanded=True)

    data["show_summaries"] = (
        True if data["frontmatter"].get("show_summaries") is not None else False
    )
    data["pages"] = []

    pages.remove("_list.md")
    for page in pages:
        p = os.path.join(directory, page)
        fn = Path(p)
        info = read_content_file(fn, expanded=True)
        summary = create_summary(info, fn, **kwargs)
        summary["frontmatter"] = info["frontmatter"]
        data["pages"].append(summary)

    return data