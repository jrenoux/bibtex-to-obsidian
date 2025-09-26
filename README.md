# bibtex-to-obsidian
This little tool allow you to create automatically an obsidian note from a bibtex entry and pre-populate it with authors

# Requirements
This tool assumes that you have a master bib file set up in `/path/to/your/master/bib/master.bib`.

# Setup
## Python Requiments
First create a python virtual environment
```bash
python3 -m venv pybtex-venv
```
and activate it using `source pybtex-venv/bin/activate` for bash, and `source pybtex-venv/bin/activate.fish` for fish.

Then install the requirements 
```
pip install -r requirements.txt
```
This will install `pybtex` and `pylatexenc`, that are needed to manipulate the bibtex entry.

## Obsidian Setup
Copy the `Paper Note.md` file in a Template folder in your obsidian vault.
From obsidian, the paper note template uses DataView to display the number of citations. If you don't want to, you can simply modify the template and remove this section.

## Setting up the variables
Open the file `create-obsidian-note.py` and modify the following variables :
- `VAULT_NAME` : the name of your obsidian vault
- `VAULT_PATH` : the path to your obsidian vault (without the name)
- `VAULT_PAPER_NOTE_FOLDER` : the relative path (in your vault) where you want your notes to be stored. For instance "Research/Paper Notes"
- `VAULT_TEMPLATE_FOLDER` : the relative path (in your vault) where you copied the `Paper Note.md` file
- `MASTER_BIB_FILE` : the absolute path of your master bib file

Then open the file `launch-create-obsidian-note.sh` and modify the `path_to_current_folder` to set it up to the folder in which you have the python and launcher files (the one of this readme if you have not moved anything).

# Usage
To create a note, simply call
```
launch-create-obsidian-note bibtexkey
```
where bibtexkey is the key of the bibtex entry you want to create the note for.

You can modify the `Template Note.md` file to fit your needs.

# For Emacs Users
You can create a function and bind that function to a key so that you can call the script from emacs and create a note from the element at point. This works from any buffer as long as your cursor is set on the bibtex key. It also works from the Ebib reference manager. Add the following to your Emacs init file :

```
(setq my-create-note-script "/path/to/current/folder/launch-create-obsidian-note.sh")

(defun my-create-obsidian-note-at-point ()
  (interactive)
  (setq obsidian (format "%s %s"  my-create-note-script (thing-at-point 'word 'no-properties)))
  (shell-command-to-string obsidian))


(global-set-key (kbd "C-c n n") 'my-create-obsidian-note-at-point)
```
