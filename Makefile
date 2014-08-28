DATABASE_USER = sfec
DATABASE_NAME = sfec
PYTHON_SRC = sfec server.py app.py

server:
	python server.py

db-init:
	# Create the database and apply the schema
	createdb $(DATABASE_NAME)
	psql $(DATABASE_NAME) < data/sql/schema-00.sql
	# Give the user the access rights to the database
	echo "GRANT ALL ON DATABASE $(DATABASE_NAME) TO $(DATABASE_USER);" | psql $(DATABASE_NAME)
	echo "GRANT ALL ON ALL TABLES IN SCHEMA public TO $(DATABASE_USER);" | psql $(DATABASE_NAME)
	echo "GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO $(DATABASE_USER);" | psql $(DATABASE_NAME)

deps: system-deps python-deps

system-deps:
	# Python
	apt-get install python-dev
	# IPython for the admin console
	apt-get install ipython
	# Postgres devel libraries
	apt-get install postgresql-server-dev-9.3

python-deps:
	# Python dependencies
	pip install -r requirements.txt

check:
	pyflakes $(PYTHON_SRC)
	pep8 $(PYTHON_SRC) --max-line-length=80

.PHONY: server deps system-deps python-deps check
