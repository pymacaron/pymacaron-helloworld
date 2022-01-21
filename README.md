# pymacaron-helloworld

A simple REST api server illustrating how to use pymacaron

See [pymacaron](https://github.com/pymacaron/pymacaron) for more information.

## Requirements

* python >= 3.8

## Start the server and run tests

Once you have checked out 'pymacaron-helloworld', install dependencies with

```shell
pip install -r requirements.txt
```

Start the server with:

```shell
python server.py --port 8080
```

To executing api tests, type in a second terminal window:

```shell
pymtest
```

All pymacaron microservices implement the default routes '/ping', '/version'
and '/auth/version', defined
[here](https://github.com/pymacaron/pymacaron/blob/master/pymacaron/ping.yaml).

## Asynchronous task

The endpoint '/async' calls a task asynchronously via celery. To see it in
action, do in one terminal:

```shell
python server.py --port 8080
```

In an other terminal:

```shell
curl http://127.0.0.1:8080/async
```

## Authentication

The endpoint '/async' calls a task asynchronously via celery. To see it in
action, do in one terminal:

```shell
python server.py --port 8080
```

In an other terminal:

```shell
curl http://127.0.0.1:8080/async
```
