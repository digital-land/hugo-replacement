#!/usr/bin/env python3

import os
import sys

from pathlib import Path
from shutil import copyfile

from frontmatter import Frontmatter

from bin.render import render
from bin.list import create_list
from bin.summary import create_summary

from digital_land_frontend.jinja import setup_jinja
from digital_land_frontend.filters import make_link
from digital_land_frontend.markdown.filter import markdown_filter
from digital_land_frontend.markdown.content_file import (
    read_content_file,
    create_breadcrumbs,
)

output_dir = "docs"
content_dir = "content"
url_root = ""

# setup jinja
env = setup_jinja()
env.globals["urlRoot"] = url_root
env.filters["make_link"] = make_link
env.filters["markdown"] = markdown_filter

content_template = env.get_template("content.html")
list_template = env.get_template("list.html")


def get_content_pages(directory):
    return os.listdir(directory)


def markdown_files_only(files, file_ext=".md"):
    return [f for f in files if f.endswith(file_ext)]


def create_output_path(fn, parent_dir=""):
    if fn.stem == "index" or fn.stem == "_index":
        return os.path.join(output_dir, parent_dir, "index.html")
    return os.path.join(output_dir, parent_dir, fn.stem, "index.html")


def render_pages(parent_dir=""):
    path_to_directory = os.path.join(content_dir, parent_dir)

    pages = get_content_pages(path_to_directory)

    for page in pages:
        p = os.path.join(path_to_directory, page)
        if os.path.isdir(p):
            # handle directories
            print(p, "is a directory")
            render_pages(os.path.join(parent_dir, page))
        elif page.endswith(".md"):
            if page == "_list.md":
                list = create_list(pages, path_to_directory)
                list["pages"].sort(key=lambda x: x["title"])
                output_path = os.path.join(output_dir, parent_dir, "index.html")
                render(
                    output_path,
                    list_template,
                    list=list,
                    breadcrumbs=create_breadcrumbs(output_path),
                )
                pass
            else:
                # compile and render markdown file
                fn = Path(p)
                contents = read_content_file(fn)
                output_path = create_output_path(fn, parent_dir)
                render(
                    output_path,
                    content_template,
                    content=contents,
                    breadcrumbs=create_breadcrumbs(output_path),
                )
        else:
            # TO DO: copy other pages to /docs
            print(p)
            # copyfile(src, dst)
            pass


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--local":
        env.globals["staticPath"] = "/static"
        url_root = ""
        env.globals["urlRoot"] = url_root

    render_pages()
