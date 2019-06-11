help:
	@echo "build: Build an image from a Dockerfile"
	@echo " test: Run the unit-tests with pytest"
	@echo "  run: Run docker run, and main.py"

build:
	@echo "running build"
	docker build -t racing_analytics .

test:
	@echo "running test"
	docker run racing_analytics py.test -s --cov-report term --cov-report html

run:
		@echo "running docker for ", $(path)
		cat $(path) | docker run -i --rm racing_analytics python main.py
