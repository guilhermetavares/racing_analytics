help:
	@echo "build: Build an image from a Dockerfile"
	@echo " test: Run the unit-tests with pytest"
	@echo "  run: Run docker run, and main.py"
	@echo "  example: Open the example file for data"

build:
	@echo "running build"
	docker build -t racing_analytics . --no-cache

test:
	@echo "running test"
	docker run racing_analytics py.test --cov-config=.coveragerc -s --cov-report term --cov-report html

run:
		@echo "running docker for ", $(path)
		cat $(path) | docker run -i --rm racing_analytics python main.py

example:
	open tests/example.txt
