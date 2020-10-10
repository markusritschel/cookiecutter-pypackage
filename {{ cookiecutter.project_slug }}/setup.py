from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest-runner',{%- endif %} ]

test_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest>=3',{%- endif %} ]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}


setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.project_version }}',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme,
{%- if cookiecutter.project_license in license_classifiers %}
    license="{{ cookiecutter.project_license }}",
{%- endif %}
    keywords=(
        "Python, {{ cookiecutter.project_slug }}"
    ),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.project_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.project_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}.*']),
    install_requires=setup_requirements,
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=False,
)
