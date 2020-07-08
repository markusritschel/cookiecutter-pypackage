{{ cookiecutter.project_name }}
=============================
![build](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/build/badge.svg)

{{ cookiecutter.project_short_description}}


Installation
------------
Clone this repo via
```
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
```
Then, in the new directory
```
cd {{ cookiecutter.project_slug }}/
```
install the package via:
```
python setup.py install
```


Testing
-------
To test the code, run `make test` in the source directory. This will execute both the unit tests and docstring examples (using pytest).

Run `make coverage` to generate a test coverage report and `make lint` to check code style consistency.


Features
--------
* [ ] TODO


Contact
-------
Regarding problems or questions please feel free to contact me via {{ cookiecutter.email }} or open an [issue](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues)
