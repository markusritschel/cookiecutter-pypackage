"""This script executes some commands after the project has been successfully set up from the cookiecutter template"""
import os
import shutil
import subprocess
from unittest.mock import DEFAULT

if not {{ cookiecutter.is_research_project }}:
    REMOVE_PATHS = [
        "data/",
        "logs/",
        "notebooks/",
        "references/",
        "reports/",
        "scripts/",
    ]
    for path in REMOVE_PATHS:
        if path and os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.unlink(path)


print("Initialize Git repository and make a first commit")
subprocess.call(['git', 'init'])
subprocess.call(['git', 'branch', '-m', 'main'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Set up new project from cookiecutter template https://github.com/markusritschel/cookiecutter-pysci-project'])

GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

DEFAULT = GREEN
CODE = BLUE

msg = f"""
    🎉 Project setup complete! How to get started:
    ----------------------------------------------

    1. Change directory into your project (if you aren't already):
         {CODE}cd {os.getcwd()}/ {DEFAULT}

    2. Activate your virtual environment (see the README.md for more details):
         On Linux/macOS: {CODE}source .venv/bin/activate {DEFAULT}
         On Windows:    {CODE}.\.venv\Scripts\activate {DEFAULT}

    3. Add a remote git repository (optional): {CODE}
         {CODE}git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }} {DEFAULT}

    4. To add packages, use:
         {CODE}uv add <package_name> {DEFAULT}

    5. To run scripts, use:
         {CODE}uv run python <script.py> {DEFAULT}

    6. To serve documentation:
         {CODE}just docs {DEFAULT}


    Happy coding! 🚀
"""


print(GREEN)
print("="*100)

print(msg)

print("")
print("="*100)
print(RESET)

