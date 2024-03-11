# Cookiecutter-PyPackage Template
[![License MIT](https://img.shields.io/github/license/markusritschel/cookiecutter-pypackage)](./LICENSE)

_A Python Package CookieCutter Template_

## Setup
This [CookieCutter](https://github.com/cookiecutter/cookiecutter) template is a boilerplate for my own personal Python projects.
It should be useful for small to medium size Python packages.

## Installation
First, install [CookieCutter](https://github.com/cookiecutter/cookiecutter) via pip or conda.
```bash
$ pip install -U cookiecutter
$ conda install -c conda-forge cookiecutter
```

## Usage
After that create a new cookiecutter from this template by executing one of the following commands:
```bash
$ cookiecutter gh:markusritschel/cookiecutter-pypackage
$ cookiecutter https://github.com/markusritschel/cookiecutter-pypackage.git
$ cookiecutter git+https://github.com/markusritschel/cookiecutter-pypackage
$ cookiecutter git+ssh://git@github.com/markusritschel/cookiecutter-pypackage.git
```

## Structure
    
    .
    ├── AUTHORS.md
    ├── CHANGELOG.md
    ├── docs
    │   ├── authors.rst
    │   ├── conf.py
    │   ├── contributing.rst
    │   ├── index.rst
    │   ├── installation.rst
    │   ├── make.bat
    │   ├── Makefile
    │   ├── readme.rst
    │   └── usage.rst
    ├── LICENSE
    ├── Makefile
    ├── MANIFEST.in
    ├── notebooks
    ├── README.md
    ├── references
    ├── requirements.txt
    ├── setup.cfg
    ├── setup.py
    ├── src
    │   └── {{ cookiecutter.package_name }}
    ├── tests
    │   ├── conftest.py
    │   ├── __init__.py
    │   └── test_{{cookiecutter.package_name}}.py
    └── tox.ini
    

### Source code
The package's source code resides in a subdirectory of `src`.
This follows the [Good Integration Practices from pytest.org](https://docs.pytest.org/en/6.2.x/goodpractices.html#choosing-a-test-layout-import-rules);
The advantage of such a layout is that the tests (residing in the root folder of the package) run always agains the 
installed version of the source code.
If the package's source code would exist in a direct subdirectory of the root directory, import statements like 
```python
import mypackage
```
would refer to the subdirectory instead of the installed version.
Another good source on this can be found [here](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure).

### Documentation
The documentation is to be placed inside `docs/` and should make use of [Sphinx](https://www.sphinx-doc.org/).


## Maintainer
- [markusritschel](https://github.com/markusritschel)

## Contributing
Issues & pull-requests accepted.


---
&copy; Markus Ritschel 2024
