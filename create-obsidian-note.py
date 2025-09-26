#!/bin/python3

import os
import sys
import platform
from pathlib import Path

from pylatexenc.latex2text import LatexNodes2Text
from pybtex.database import parse_file

VAULT_NAME = "my-vault"
VAULT_PATH = "/path/to/your/obsidian/vault/"
VAULT_PAPER_NOTE_FOLDER = "path/to/your/note/folder/"
VAULT_TEMPLATE_FOLDER = "path/to/your/template/folder"
MASTER_BIB_FILE = "/path/to/your/master/bibfile/master.bib"


def __main__(args):
    bibtex_key = args[1]
    bib_data = parse_file(MASTER_BIB_FILE)
    entry = bib_data.entries[bibtex_key]
    title = entry.fields['title']
    title = title.replace('{', '').replace("}", "").replace(":", "").replace("'", "").replace('"', '').replace("?", "").replace("/","-")

    # getting the template from obsidian
    template_file = f"{VAULT_PATH}/{VAULT_TEMPLATE_FOLDER}/Paper Note.md"
    template = open(template_file).read()

    #Replace the <bibtex-key> in the template by the actual bibtex key
    note = template.replace("%bibtex-key%", bibtex_key)

    #Replace %title% by the title
    note = note.replace("%title%", title)
    print(entry.fields)
    
    author = []
    for a in entry.persons['author']:
        author.append(f"  - {LatexNodes2Text().latex_to_text(str(a))}")
    author_str = "\n".join(author)
    note = note.replace("%author%", author_str)


    # Create the actual note
    filename = f"{bibtex_key}"
    note_file = f"{VAULT_PATH}/{VAULT_PAPER_NOTE_FOLDER}/{filename}.md"

    if not Path(note_file).is_file():
        # print("Creating vault note: " + note_file)
        with open(note_file, 'w') as f:
            f.write(note)

            #f.write("---\n")
            #f.write(f"bibtex-key: {bibtex_key}\n")
            #f.write("tags:\n")
            #f.write(f"  - Paper\n")
            #f.write("---\n\n\n")
            #f.write("## Citations\n\n")
            #f.write("```query\n")
            #f.write(f"content:{bibtex_key} -[bibtex-key:{bibtex_key}]\n")
            #f.write("```\n")

    if platform.system() == "Linux":
        url = f"'obsidian://open?vault={VAULT_NAME}&file='{VAULT_PAPER_NOTE_FOLDER}{filename}''"
        url = url.replace(" ", "%20")
        os.system(f"open {url}")
    elif platform.system() == "Windows":
        url = f'obsidian://open?vault={VAULT_NAME}&file="{VAULT_PAPER_NOTE_FOLDER}{filename}"'
        url = url.replace(" ", "%20")
        os.startfile(url)
    else:
        raise Exception("Unsupported platform")

    print(url)


if __name__ == "__main__":
    __main__(sys.argv)
