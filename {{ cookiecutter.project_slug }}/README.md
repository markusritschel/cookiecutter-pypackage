# {{ cookiecutter.project_name }}

![build](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/build/badge.svg)
{% if cookiecutter.project_license != "No License" %}[![License {{ cookiecutter.project_license }}](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})](./LICENSE){% endif %}


{{ cookiecutter.project_short_description}}


## Installation
Clone this repo via
```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
```
Then, in the new directory (`cd {{ cookiecutter.project_slug }}/`) install the package via:
```
python setup.py install
```
or via
```
python setup.py develop
```
if you plan on making changes on the code.


## Testing
To test the code, run `make test` in the source directory.
This will execute both the unit tests and docstring examples (using pytest).

Run `make coverage` to generate a test coverage report and `make lint` to check code style consistency.


## Features
* [ ] TODO


## Maintainer
- [markusritschel](https://github.com/markusritschel)


## Contact & Issues
For any questions or issues, please contact me via {{ cookiecutter.email }} or open an [issue](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues).


---
&copy; {{ cookiecutter.project_author }} {% now 'local', '%Y' %}
