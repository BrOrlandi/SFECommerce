SFECommerce
===========

Simple Flask E-Commerce (SFEC) developed with Flask Python microframework for academic purpose only

Authors
-------

- [Bruno Orlandi](https://github.com/BrOrlandi) (brorlandi@gmail.com)
- [Nihey Takizawa](https://github.com/nihey) (nihey.takizawa@gmail.com)
- [Gustavo Consentini](https://github.com/gconsentini) (gustavoconsentini@gmail.com)



UML
---

![UML](https://raw.githubusercontent.com/BrOrlandi/SFECommerce/master/uml_diagram.png "UML")

Setup Instructions
------------------

Must have **pip** installed!

# Dependencies
* `make system-deps` # Install system dependencies (may require root)
* Create a virtualenv called `env` and activate it.
* `make python-deps` # Install python dependencies

# Database
* `python sfecadmin.py dbinit`  Will create the SQL Schema and create the database.sqlite

# Executing
* `python server.py`
