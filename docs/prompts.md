# Prompts

When creating your project from this template, CookieCutter will give you a few prompts you need to answer.
All the information you give there can be changed afterward. However, certain names such as `package_name` occur in various places (including directory names) and might be cumbersome to search and replace.

- **project_author** <br />
    This should be your full name. It will be used in documentation and project meta information.
- **email** <br />
    Your e-mail address. Will also be mostly used for meta information.
- **github_username** <br />
    Your github username. Will also be mostly used for meta information but also for generating links to your repository.
- **project_name** <br />
    Give the project a concise and meaningful name. This can be capitalized (e.g. "My new Project")
- **project_slug** <br />
    This should match your project name, without blanks in the name. The script will default this with a version of `project_name`, blanks replaced by dashes. 
- **package_name** <br />
    This is the name for your python package. You will use this in import statements. Hence, it should comply to Python naming standards, e.g. no blanks, no dashes,...)
- **is_research_project** `[y/n] (y)`: <br />
    If answered yith `yes`, your project will contain certain directories and files that are useful for typical research projects in python.
    If you answer this question with `no`, these redundant files are removed. This might be useful if you want to create a pure python package.
- **project_description** <br />
    Here, give a concise description of what your package/project is about. Will be used in meta information, documentation, etc.
- **project_version** [default: `0.1.0`] <br />
    Here, give the initial version information. It should follow the standard format `RELEASE.MAJOR.MINOR`. See also <!-- TODO -->
- **Select command_line_interface**
    Select between different CLI options
    ```
    1 - Click
    2 - Docopt
    3 - No command-line interface
    ```
- **Select project_license**
    ```
    1 - MIT license
    2 - BSD license
    3 - ISC license
    4 - Apache Software License 2.0
    5 - GNU General Public License v3
    6 - Not open source
    ```
- **Select docs_engine**
    ```
    1 - Sphinx
    2 - Zensical
    3 - MyST
    ```