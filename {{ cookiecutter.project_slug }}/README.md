# {{ cookiecutter.project_name }}

[![build](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/main.yml/badge.svg)]([![build](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/main.yml/badge.svg)
)
{% if cookiecutter.project_license != "No License" %}[![License {{ cookiecutter.project_license }}](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})](./LICENSE){% endif %}


{{ cookiecutter.project_short_description}}


## Installation
Clone this repo via
```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
```
Then, in the new directory (`cd {{ cookiecutter.project_slug }}/`) install the package via:
```
pip install .
```
or via
```
pip install -e .
```
if you plan on making changes to the code.

Alternatively, install directly from GitHub via
```
pip install 'git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git'
```

## Testing
Run `make tests` in the source directory to test the code.
This will execute both the unit tests and docstring examples (using `pytest`).

Run `make lint` to check code style consistency.



## Maintainer
- [{{ cookiecutter.github_username }}](https://github.com/{{ cookiecutter.github_username }})


## Contact & Issues
For any questions or issues, please contact me via {{ cookiecutter.email }} or open an [issue](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues).


---
&copy; {{ cookiecutter.project_author }} {% now 'local', '%Y' %}
