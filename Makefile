help:
	@echo "running help"

build:
	@echo "running build"
	docker build -t racing_analytics .

test:
	@echo "running test"

run:
		@echo "running run"
		# docker run racing_analytics
		docker run -it --rm -v $PWD/somefile.txt:/foo_copy.txt racing_analytics python script.py

mkdir:
	docker run racing_analytics
	docker exec -i racing_analytics sh -c 'mkdir -p /home/e1/e2'
