

DOCKER_COMPOSE=docker/development/docker-dev.yml
DOCKER_COMPOSE_PRODUCTION=docker/production/docker-prod.yml

check.compose_file:
	@if test "$(COMPOSE_FILE)" = "" ; then echo "COMPOSE_FILE is undefined \nTry: make dev or homolog"; exit 1; fi

dev:
	$(eval COMPOSE_FILE:=$(DOCKER_COMPOSE))

prod:
	$(eval COMPOSE_FILE:=$(DOCKER_COMPOSE_PRODUCTION))

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

clean-others:
	@find . -name 'Thumbs.db' -exec rm -f {} \;

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean: clean-build clean-others clean-pyc

createsuperuser: check.compose_file
	@docker-compose -f $(COMPOSE_FILE) exec news_provider_api python manage.py createsuperuser

down: check.compose_file
	@docker-compose -f $(COMPOSE_FILE) down

makemig: check.compose_file
	@docker-compose -f $(COMPOSE_FILE) exec news_provider_api python manage.py makemigrations

mig: check.compose_file
	@docker-compose -f $(COMPOSE_FILE) exec news_provider_api python manage.py migrate

run: check.compose_file
	@docker-compose -f $(COMPOSE_FILE) build
	@docker-compose -f $(COMPOSE_FILE) up -d

shell: check.compose_file
	@docker-compose -f $(COMPOSE_FILE) run news_provider_api python manage.py shell

build: check.compose_file
	@docker-compose -f $(COMPOSE_FILE) build

up: check.compose_file
	@docker-compose -f $(COMPOSE_FILE) up
