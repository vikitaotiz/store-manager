# store-manager
[![Build Status](https://travis-ci.org/vikitaotiz/store-manager.svg?branch=master)](https://travis-ci.org/vikitaotiz/store-manager)
[![Coverage Status](https://coveralls.io/repos/github/vikitaotiz/store-manager/badge.svg?branch=master)](https://coveralls.io/github/vikitaotiz/store-manager?branch=master)

Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.

How to manually test

$ pip install virtualenv

NB This install virtualenv Globally(virtual environment allows you to create independent env isolated from your actual physical machine)

$ virtualenv -p python3 env

$ source env/bin/activate

Clone this repository: $ https://github.com/vikitaotiz/store-manager.git

navigate into the repository after cloning

$ git checkout Develop to switch from master to this branch

$ pip install -r requirements.txt

$ python orders.py

# Endpoints are

 | Method         | Endpoint       | Description            |
 |----------------|----------------|------------------------|
 | Get            | api/v1/products      | Gets all products      |
 | Get            | api/v1/product/1     | Get single a product   |
 | Post           | api/v1/products      | Adds a product         |
 | Get            | api/v1/orders        | Gets all sales orders  |
 | Get            | api/v1/order/1       | Gets single sale order |
 | Post           | api/v1/orders        | Adds a sale order      |
