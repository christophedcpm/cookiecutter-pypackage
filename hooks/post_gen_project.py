#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath):
    os.removedirs(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.rst")
        remove_file("docs/authors.rst")

    if "{{ cookiecutter.ci_provider }}" == "Github Action":
        remove_file(".travis.yml")
        if '{{cookiecutter.enable_automatic_pypi_deployment }}' == 'n':
            remove_file('.github/workflows/publish.yml')

    if "{{ cookiecutter.ci_provider }}" == "Travis-CI":
        remove_dir(".github")

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("{{ cookiecutter.project_slug }}", "cli.py")
        remove_file(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")
