.PHONY: start down build restart logs shell makemigrations migrate createsuperuser create_dump load_dump

start:
	docker-compose up --build

down:
	docker-compose down

build:
	docker-compose build

logs:
	docker-compose logs -f

shell:
	docker-compose exec app bash

makemigrations:
	docker-compose exec app python manage.py makemigrations

migrate:
	docker-compose exec app python manage.py migrate

createsuperuser:
	docker-compose exec app python manage.py createsuperuser

create_dump:
	docker-compose up -d
	docker-compose exec app sh -c "mkdir -p /tmp/dump && python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > /tmp/dump/dump.json"
	docker cp $$(docker-compose ps -q app):/tmp/dump/dump.json test_db/dump.json
	docker-compose down

load_dump:
	docker-compose up -d
	docker-compose exec app python manage.py loaddata test_db/dump.json
	docker-compose down
