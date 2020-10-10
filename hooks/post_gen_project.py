import subprocess

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print("Add remote repository https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git")
subprocess.call(['git', 'remote', 'add', 'origin', 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git'])

# print("Try pushing to remote repository")
# try:
#     subprocess.call(['git', 'push', '-u', 'origin', 'master'])
# except:
#     print("Pushing failed! Couldn't reach remote repository https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git!")
