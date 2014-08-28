SFECommerce
===========

Simple Flask E-Commerce (SFEC) developed with Flask Python microframework for academic purpose only

Authors
-------

Bruno Orlandi (brorlandi@gmail.com)
Nihey Takizawa (nihey.takizawa@gmail.com)

UML
---

![UML](https://raw.githubusercontent.com/BrOrlandi/SFECommerce/master/uml_diagram.png "UML")

Setup Instructions
------------------

# Dependencies
* make system-deps # Install system dependencies (may require root)
* make python-deps # Install python dependencies

# Database
* createuser sfec # Create a SFEC postgres database user
* make init-db # Appy the database schema

# Executing
* python server.py
