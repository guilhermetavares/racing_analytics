help:
	@echo "running help"

build:
	@echo "running build"
	docker build -t racing_analytics . # --no-cache

test:
	@echo "running test"
	docker run racing_analytics py.test tests.py -s --cov-report term --cov-report html

run:
		@echo "running docker for ", $(path)
		cat $(path) | docker run -i --rm racing_analytics python main.py
