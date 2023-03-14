PROJECT = python
SERVICE = api

build:
	docker build -t ${PROJECT}-${SERVICE} .

run:
	docker-compose up