# pymacaron-helloworld

A super simple REST api server illustrating how to use pymacaron

See [pymacaron](https://github.com/pymacaron/pymacaron) for more information.

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
