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
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/  
lint:
	poetry run flake8 gendiff
.PHONY: gendiff