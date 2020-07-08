export SHELL := /bin/bash

test:
	pytest -n auto --doctest-modules {{ cookiecutter.package_name }}

coverage:
	pytest -n auto --doctest-modules --cov=seaborn --cov-config=.coveragerc {{ cookiecutter.package_name }}

lint:
	flake8 {{ cookiecutter.package_name }}
