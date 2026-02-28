# Cookiecutter-PyPackage Template
[![License MIT](https://img.shields.io/github/license/markusritschel/cookiecutter-pypackage)](./LICENSE)

This [CookieCutter](https://github.com/cookiecutter/cookiecutter) template is a boilerplate for small to medium-sized Python projects.
It should be used for small to medium size Python packages.
Depending on the responses to the initial prompts, it can create a boilerplate for data science projects, or for a general Python package.

## Get started
The easiest way to get started is to use [uv](https://docs.astral.sh/uv/0).
Make sure you have `uv` installed, and then run the following command to create a new project from this template:
```bash
$ uvx cookiecutter gh:markusritschel/cookiecutter-pypackage
```

<details>
<summary>Alternatively, without uv</summary>

install [CookieCutter](https://github.com/cookiecutter/cookiecutter) via pip or conda, and then run the following command to create a new project from this template:
```bash
$ cookiecutter gh:markusritschel/cookiecutter-pypackage
```

</details>

<!-- 
```bash
$ cookiecutter gh:markusritschel/cookiecutter-pypackage
$ cookiecutter https://github.com/markusritschel/cookiecutter-pypackage.git
$ cookiecutter git+https://github.com/markusritschel/cookiecutter-pypackage
$ cookiecutter git+ssh://git@github.com/markusritschel/cookiecutter-pypackage.git
``` 
-->

## What's in for you?

### Tools

| Purpose               | Tool     | Comment                                             |
| --------------------- | -------- | --------------------------------------------------- |
| Dependency management | `uv`     | A modern and blazingly fast Python package manager  |
| Version control       | `git`    | The most popular version control system (VCS)       |
| Documentation         | `Sphinx` | A popular and versatile docs generator for Python   |
| Code quality          | `ruff`   | A fast linter and code formatter for Python         |
| Testing               | `pytest` | A powerful testing framework for Python             |
| Task automation       | `just`   | A modern alternative to Makefiles                   |
| Test Github Actions   | `act`    | A tool to run GitHub Actions locally                |


### Structure

```
├── assets/
├── CHANGELOG.md
├── CITATION.cff
├── data
│   ├── interim/
│   ├── processed/
│   └── raw/
├── docs/
│   ├── _config/
│   ├── conf.py
│   ├── references.bib
│   └── _static/
├── justfile
├── LICENSE
├── logs/
├── Makefile
├── notebooks/
│   ├── exploratory/
│   ├── jupyter_startup.ipy
│   └── reports/
├── pyproject.toml
├── README.md
├── references/
├── reports/
│   ├── figures/
│   └── README.md
├── ruff.toml
├── scripts/
├── src/
│   └── <package_name>/
└── tests/
```


### Source code
The project follows a `src` layout, which means that the package's source code resides in a subdirectory of `src`.
This follows the [Good Integration Practices from pytest.org](https://docs.pytest.org/en/6.2.x/goodpractices.html#choosing-a-test-layout-import-rules) and is a common and recommended layout for Python project;
it helpso avoid issues with imports and ensures that the installed version of the package is always used during development and testing.
<!-- If the package's source code would exist in a direct subdirectory of the root directory, import statements like 
```python
import mypackage
```
would refer to the subdirectory instead of the installed version. -->
Further reading on this can be found [here](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure) or [here](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).


### Project documentation
The documentation is to be placed inside `docs/` and makes use of Sphinx.

<!-- The documentation of this repository is made with [Zensical](https://zensical.org/). -->

***

## Maintainer & Contribution
[markusritschel](https://github.com/markusritschel) maintains this project. \
Issues & pull-requests accepted.

## Documentation
Documentation for this CookieCutter template is available at https://markusritschel.github.io/cookiecutter-pypackage

---
&copy; Markus Ritschel 2026
