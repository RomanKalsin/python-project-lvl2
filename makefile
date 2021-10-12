install:
	poetry install
gendiff:
	poetry run gendiff
build:
	poetry build
package-install:
	python3 -m pip install --user dist/*.whl
package-uninstall:
	python3 -m pip uninstall hexlet-code
test:
	poetry run pytest
lint:
	poetry run flake8 gendiff