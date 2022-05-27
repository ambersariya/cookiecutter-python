all: test

test: create-project 

create-project:
	cookiecutter cookiecutter-python --directory=some_project_name --no-input --overwrite-if-exists -v

test-project:
	cd some_project_name

install-dependencies:
	make