# 🍪 Python Cookie Cutter

A configurable python project template to help get started. 

## Features:

- There is no framework at all and is left open for you to add libraries. 
- There is no poetry.lock file checked in, so you can have latest set of libraries at that time.
- Uses Makefile and has alot of targets for your day to day workflow
- Uses .editorconfig

The template only contains the following dependencies.

```toml
[tool.poetry.dependencies]
python = "^{{cookiecutter.python_version}}"

[tool.poetry.dev-dependencies]
pytest = "^5.2"
black = "^22.1.0"
flake8 = "^3.8.4"
mypy = "^0.960"
isort = "^5.10.1"
```

## Install

```bash
pip install cookiecutter
```

## Create project

```bash
🍪 $ cookiecutter https://github.com/ambersariya/cookiecutter-python

You've downloaded ~/.cookiecutters/cookiecutter-python before. Is it okay to delete and re-download it? [yes]: no
Do you want to re-use the existing version? [yes]: yes
project_name [some project name]: example_proj
project_short_description [A project to]: Captures screenshots of webpages
project_slug [example_proj]:
package_slug [example_proj]:
python_version [3.9.7]:
package_manager [poetry]:
version [0.1.0]:
full_name [Firstname Lastname]: Firstname Lastname
email [username@example.org]: firstname lastname
license []:

🍪 $
```
## Test

Change into your newly created project directory and simply run the following to check if everything installed properly.

```bash
🍪 $ make
```

## Push Project

When the project scaffolding has been created, please ensure to create a new repo/project. Then grab git repository remote details and `git push`
