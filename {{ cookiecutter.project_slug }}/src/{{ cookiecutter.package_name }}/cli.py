#!/usr/bin/env python
# -*- coding utf-8 -*-
#
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Author: {{ cookiecutter.project_author }}
# eMail:  {{ cookiecutter.email }}
# Date:   {% now 'local', '%Y-%m-%d' %}
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
"""Console script for {{cookiecutter.project_slug}}."""

from __future__ import absolute_import, division, print_function, with_statement

{%- if cookiecutter.command_line_interface|lower == 'docopt' %}
import docopt
{%- endif %}
import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return None
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'docopt' %}
def main():
    """Console script for {{cookiecutter.project_slug}}."""
    return None
{%- endif %}


if __name__ == "__main__":
    sys.exit(main())
