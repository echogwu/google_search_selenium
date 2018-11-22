# Purpose

this repos is for plastiq QA challenge


# How to run it

* Prepare your browser
To turn on WebDriver support, do the following: Ensure that the Develop menu is available. It can be turned on by opening Safari preferences (Safari > Preferences in the menu bar), going to the Advanced tab, and ensuring that the Show Develop menu in menu bar checkbox is checked

* Get Run Env ready
    * Install python3
    * create a virtual environment

    ```plastiq git:(master) ✗ python3 -m venv py3venv```
    * activate the virtual environment and install dependency package within it

    ```plastiq git:(master) ✗ source py3venv/bin/activate
    plastiq git:(master) ✗ pip3 install -r requirements.txt
    ```
    * check the help info before you run the script

    ```plastiq git:(master) ✗ python google_search.py -h```
    * run it

    ```plastiq git:(master) ✗  python google_search.py --search "test automation is awesome" --sleep 5```
* Misc

If your team is not using the same IDE with the same formatting setup, you can all use command line to push your commits. 

```plastiq git:(master) ✗ bin/setup_yapf```

This will download and set up the pre-commit for your current repo. Only run this script once for all.

The git pre-commit hook automatically formats your Python files before they are committed to your local repository. Any changes yapf makes to the files will stay unstaged so that you can diff them manually before you push them to remote.
