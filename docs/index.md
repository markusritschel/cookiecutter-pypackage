---
icon: material/rocket-launch
---

<!-- https://fpgmaas.github.io/cookiecutter-uv/ -->
# Cookiecutter PyProject :simple-pythonanywhere:


This is a [CookieCutter](https://www.cookiecutter.io/) template for Python projects.
It uses modern tools for development, testing, and packaging.
Depending on the responses to the [initial prompts](prompts), it can create a boilerplate for data science projects or for a general Python package.

??? note "Requirements"
    To use this template, you need to have [CookieCutter](https://www.cookiecutter.io/) available on your machine.
    Either install it globally via pip or conda, or use `uv` to run it without the need of installing it.
    The latter is recommended.

## Quickstart
To get started, simply run
```bash
uvx cookiecutter gh:markusritschel/cookiecutter-pypackage
```
and follow the [prompts](prompts) to customize your project.
Once finished, navigate into the created directory to start working on your new Python project!

??? note "Without uv"
    If you don't want to use uv, you can also install CookieCutter globally and run it with the following command:
    ```bash
    cookiecutter gh:markusritschel/cookiecutter-pypackage
    ```


## Features

This template comes ready with a selection of modern and useful tools:

- **[Development Workflow](features/development.md)** – A collection of useful tools for an efficient development flow. 
[uv](https://docs.astral.sh/uv/) helps you manage your package dependencies (it's *a lot* faster than conda). 
Use [pytest](https://pytest.org/) to run your own tests and get coverage information.
The _src layout_ ensures that only the installed version of your code is tested.
State-of-the-art version control through git integration helps you keep track of your code changes. 
[justfile](https://just.systems/) is a modern taskrunner. Use it as an alternative for Make.
[GitHub Actions](https://github.com/features/actions) for CI/CD can automate a lot of things such as auto-deploying your documentation via Github pages, testing your code on every push, etc.
DevContainer support allows you to code in a containered environment for an extra layer of security.
- **[Code Quality](features/code-quality.md)** – Tools for ensuring code quality include Ruff for linting/formatting, ty for type checking, pytest for testing.
- **[Package Management](features/uv.md)** – uv for dependency management and virtual environments.
- **[Documentation](features/documentation.md)** – Sphinx with MyST Markdown, autoapi, bibliography support, and GitHub Pages deployment.
- **[Task Automation](features/justfile.md)** – Just for simplified development task execution.
- **[GitHub Actions CI/CD](features/github-actions.md)** – Automated testing, linting, and documentation deployment.
- **[Publishing](features/publish-package.md)** – PyPI package publishing with automated workflows.
- **[Research Projects](features/research-projects.md)** – Optional data science project structure (`data/`, `notebooks/`, `reports/`).

| Tool/Feature   | Category                                  |
| -------------- | ----------------------------------------- |
| `uv`           | Dependency management & packaging         |
| `pytest`       | Testing and code coverage                 |
| github actions | Continuous Integration                    |
| dependabot.yml | Dependabot configuration for gh actions   |
| `ruff`         | Code linting and formatting               |
| `ty`           | Type hints                                |
| DevContainer   | Development container for VSCode          |
| justfile       | Task automation (modern Make alternative) |


## How to continue

Read the [Tutorial](./tutorial) for a step-by-step guide to create a new project.
In the features section you can find detailed documentation for each tool and feature (links above).
