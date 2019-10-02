# pymacaron-helloworld

A super simple REST api server illustrating how to use pymacaron

See [pymacaron](https://github.com/pymacaron/pymacaron) for more information.

## Start the server and run tests

Once you have checked out 'pymacaron-helloworld', start by running the server
and executing its api tests to make sure all is in order.

In one terminal, do:

```shell
python server.py --port 8080
```

In a second terminal, do:

```shell
pymtest
```

All pymacaron microservices implement the default routes 'v1/ping',
'v1/version' and 'v1/auth/version', defined [here](https://github.com/pymacaron/pymacaron/blob/master/pymacaron/ping.yaml).

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
