help:
	@echo "running help"

build:
	@echo "running build"
	docker build -t racing_analytics . --no-cache

test:
	@echo "running test"
	docker run racing_analytics py.test src/tests.py -s --cov-report term --cov-report html

run:
		@echo "running run"
		# docker run racing_analytics
		# docker run -it --rm -v $PWD/example.txt:/foo_copy.txt racing_analytics python script.py
		cat example.txt | docker run -i --rm racing_analytics python main.py

mkdir:
	docker run racing_analytics
	docker exec -i racing_analytics:latest sh -c 'mkdir -p /home/e1/e2'
