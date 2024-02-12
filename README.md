# Django Backend API

## Description

This repository contains the Django backend API for blog-app.

### Requirements
- docker client, docker daemon, and docker-compose
(you can install Docker Desktop at the [docker website](https://www.docker.com) to get all of them)

### Run
<hr style="border: 0; height: 1px; margin: 0 0 10px 0">

clone the repo and cd to the project's root directory.
1. run and setup
- `docker-compose up -d` to build and spin-up the containers in detached mode (as a background process)
- `docker-compose exec api python manage.py migrate` to setup the db
```
python manage.py seed
```
2. (Optional) seed the db with mock data
- `docker-compose exec api python manage.py seed 100` 
seeds the db with 100 mock posts

3. interact with the api at `localhost:8000/api/`

### Run the tests
<hr style="border: 0; height: 1px; margin: 0 0 10px 0">

run `docker-compose exec api python manage.py test`

### REST API
<hr style="border: 0; height: 1px; margin: 0 0 10px 0">

1. Read
- list all blogs posts at
`/api/posts/`
- get individual blog posts at
`/api/posts/<post_id>/`
