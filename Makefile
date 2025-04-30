build:
	docker build -t qa-tests .

test:
	docker run qa-tests

debug:
	docker run -it --entrypoint bash qa-tests

report:
	mkdir -p reports && docker run -v $(PWD)/reports:/app/reports qa-tests
