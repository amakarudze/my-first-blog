[![codecov](https://codecov.io/gh/amakarudze/my-first-blog/branch/main/graph/badge.svg?token=WSeKNkk3gx)](https://codecov.io/gh/amakarudze/my-first-blog)

# My personal blog

This my personal blog I am developing while exploring Python and Django more. The online version is available at 
https://www.makarudze.com.

## Requirements
This blog requires the following:
* Django 4.0+ 
* MySQL
* Python 3.9+

## Installation
1. Clone this repo.
2. Create a virtual environment.
3. Install pip-tools.
4. Install required packages by running `pip install -r requirements.txt`.
5. Create a MySQL database. 
6. Edit the `.env-example` with your environment variables, including database name and run migrations.
7. To make changes to the  `requirements.txt`, edit `requirements.in` then run `pip-compile` to generate an updated `requirements.txt`.

## Run Tests
* Run `coverage run -m pytest` to run tests.

## Usage
1. Create a superuser.
2. Login through Django admin and add posts and all other content.
