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

Endpoints are

Get /products 

Get /product/1

Post /products

Get /orders

Get /order/1

Post /orders
