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
		docker run -it --rm -v $(FILE):/files racing_analytics python script.py data.txt

up:
	docker cp foo.txt racing_analytics:/foo_copy.txt
