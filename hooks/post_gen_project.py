import subprocess

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

subprocess.call(['git', 'remote', 'add', 'origin', 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git'])
try:
    subprocess.call(['git', 'push', '-u', 'remote', 'master'])
except:
    print("Couldn't reach remote repository https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git")
