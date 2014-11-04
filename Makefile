PYTHON_SRC = sfec server.py app.py

server:
	python server.py

deps: system-deps python-deps

system-deps:
	# Python
	apt-get install python-dev
	# IPython for the admin console
	apt-get install ipython

python-deps:
	# Python dependencies
	pip install -r requirements.txt

check:
	pyflakes $(PYTHON_SRC)
	pep8 $(PYTHON_SRC) --max-line-length=80
	python sfecadmin.py test

.PHONY: server deps system-deps python-deps check
