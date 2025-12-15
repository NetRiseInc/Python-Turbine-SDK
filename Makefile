.PHONY: install generate test build clean

install:
	poetry install

generate:
	poetry run ariadne-codegen

test:
	poetry run pytest

build:
	poetry build

clean:
	rm -rf dist .pytest_cache src/netrise_turbine_sdk_graphql
