VENV=./ve
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
FLAKE8=$(VENV)/bin/flake8
CODEGEN_VERSION=2.2.3
CODEGEN=java -jar swagger-codegen-cli-$(CODEGEN_VERSION).jar generate
USER_DATA_STORE_CLIENT_DIR=user_data_store_client

# Colours.
CLEAR=\033[0m
RED=\033[0;31m
GREEN=\033[0;32m
CYAN=\033[0;36m

.SILENT: docs-build
.PHONY: check

help:
	@echo "usage: make <target>"
	@echo "    $(CYAN)build-virtualenv$(CLEAR): Creates virtualenv directory, 've/', in project root."
	@echo "    $(CYAN)clean-virtualenv$(CLEAR): Deletes 've/' directory in project root."
	@echo "    $(CYAN)docs-build$(CLEAR): Build documents and place html output in docs root."
	@echo "    $(CYAN)mock-user-data-store-api$(CLEAR): Starts Prism mock server for the User Data Store API."
	@echo "    $(CYAN)validate-swagger$(CLEAR): Check Swagger spec for errors."
	@echo "    $(CYAN)user-data-store-client$(CLEAR): Generate a client for the User Data Store API."
	@echo "    $(CYAN)user-data-store-api$(CLEAN): Generate a Flask server for the User Data Store API."



$(VENV):
	@echo "$(CYAN)Initialise base ve...$(CLEAR)"
	virtualenv $(VENV) -p python3.5
	@echo "$(GREEN)DONE$(CLEAR)"

# Creates the virtual environment.
build-virtualenv: $(VENV)
	@echo "$(CYAN)Building virtualenv...$(CLEAR)"
	# TODO: Depending on project type, requirements will need to be installed here.
	@echo "$(GREEN)DONE$(CLEAR)"

# Deletes the virtual environment.
clean-virtualenv:
	@echo "$(CYAN)Clearing virtualenv...$(CLEAR)"
	rm -rf $(VENV)
	@echo "$(GREEN)DONE$(CLEAR)"

# Build sphinx docs, then move them to docs/ root for GitHub Pages usage.
docs-build:  $(VENV)
	@echo "$(CYAN)Installing Sphinx requirements...$(CLEAR)"
	$(PIP) install sphinx sphinx-autobuild
	@echo "$(GREEN)DONE$(CLEAR)"
	@echo "$(CYAN)Backing up docs/ directory content...$(CLEAR)"
	tar -cvf backup.tar docs/source docs/Makefile
	@echo "$(GREEN)DONE$(CLEAR)"
	@echo "$(CYAN)Clearing out docs/ directory content...$(CLEAR)"
	rm -rf docs/
	@echo "$(GREEN)DONE$(CLEAR)"
	@echo "$(CYAN)Restoring base docs/ directory content...$(CLEAR)"
	tar -xvf backup.tar
	@echo "$(GREEN)DONE$(CLEAR)"
	# Remove the tar file.
	rm backup.tar
	# Actually make html from index.rst
	@echo "$(CYAN)Running sphinx command...$(CLEAR)"
	$(MAKE) -C docs/ clean html SPHINXBUILD=../$(VENV)/bin/sphinx-build
	@echo "$(GREEN)DONE$(CLEAR)"
	@echo "$(CYAN)Moving build files to docs/ root...$(CLEAR)"
	cp -r docs/build/html/. docs/
	rm -rf docs/build/
	@echo "$(GREEN)DONE$(CLEAR)"

prism:
	curl -L https://github.com/stoplightio/prism/releases/download/v0.6.21/prism_linux_amd64 -o prism
	chmod +x prism

mock-user-data-store-api: prism
	./prism run --mockDynamic --list -s swagger/user_data_store.yml -p 8010

validate-swagger: prism
	@./prism validate -s swagger/user_data_store.yml && echo "The Swagger spec contains no errors"

swagger-codegen-cli-$(CODEGEN_VERSION).jar:
	wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/$(CODEGEN_VERSION)/swagger-codegen-cli-$(CODEGEN_VERSION).jar

# Generate the client code to interface with the User Data Store
user-data-store-client: swagger-codegen-cli-$(CODEGEN_VERSION).jar
	@echo "$(CYAN)Generating the client for the User Data Store API...$(CLEAR)"
	$(CODEGEN) -l python -i swagger/user_data_store.yml -o /tmp/$(USER_DATA_STORE_CLIENT_DIR)
	cp -r /tmp/$(USER_DATA_STORE_CLIENT_DIR)/swagger_client* $(USER_DATA_STORE_CLIENT_DIR)
	rm -rf /tmp/$(USER_DATA_STORE_CLIENT_DIR)

# Generate the flask server code for the User Data Store
user-data-store-api: swagger-codegen-cli-$(CODEGEN_VERSION).jar validate-swagger
	@echo "$(CYAN)Generating flask server for the User Data Store API...$(CLEAR)"
	$(CODEGEN) -i swagger/user_data_store.yml -l python-flask -o .

$(FLAKE8): $(VENV)
	$(PIP) install flake8

check: $(FLAKE8)
	$(FLAKE8)

create-tables:
	@echo "$(CYAN)Creating tables$(CLEAR)"
	$(PYTHON) models.py
