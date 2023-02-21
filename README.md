# dino-api

This repository demonstrates the following engineering flow for API development:

1. Define new endpoint(s) in OpenAPI (found at [api/docs/openapi.yaml](./api/docs/openapi.yaml))
2. Generate and run contract tests from spec (see [here](#generating-and-running-contract-tests)). They should fail.
3. Implement new endpoint(s)
4. Repeat Step 2. They should pass!

## Building the Docker Image

To build the Docker image containing the API:

```shell
docker build -t dino-api:local .
```

## Starting the database locally

The app is configured to work with PostgreSQL 13. To start the database, use the following:

```bash
docker run -d --name postgres \
  -e POSTGRESQL_DATABASE=dino \
  -e POSTGRESQL_USERNAME=dino \
  -e POSTGRESQL_PASSWORD=password \
  -p 5432:5432 \
  bitnami/postgresql:13
```

## Migrating the Database

```shell
docker run -v $(pwd)/db:/usr/app/db dino-api:local python manage.py migrate
```

## Running the API

To run the API after starting and migrating the database:

```shell
docker run -p 8000:8000 -v $(pwd)/db:/usr/app/db dino-api:local
```

## Viewing the API Docs:

To view the generated API documentation after starting the API, navigate to [localhost:8000/api/docs/](http://localhost:8000/api/docs/).

## Generating and Running Contract Tests

To run contract tests after starting the API:

```shell
docker run \
  -v $(pwd)/api/docs:/api \
  apiaryio/dredd \
  dredd /api/openapi.yaml http://host.docker.internal:8000
```
