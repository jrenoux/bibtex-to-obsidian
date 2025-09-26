#!/bin/bash
#format: launch-create-obsidian-note bibtexkey

# settings
path_to_current_folder="/path/to/current/folder"

# get the key from the arguments
key=$1

#source the environment
source $path_to_current_folder/pybtex-venv/bin/activate

#launch the python script
python3 $path_to_current_folder/create-obsidian-note.py $key
