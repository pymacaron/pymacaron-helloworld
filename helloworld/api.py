import logging
import time
from pymacaron_async import asynctask
from pymacaron_core.swagger.apipool import ApiPool


log = logging.getLogger(__name__)


def do_hello():
    """Replies to a call to /hello"""
    return ApiPool.helloworld.model.Hello(message='Hello world!')


#
# The following methods are for educational purpose only.
# Remove them when cloning helloworld to bootstrap your own microservice.
#

def do_crash():
    """Call /die and see how pymacaron handles an exception"""
    raise Exception("OH! NO! I JUST DIED!!")


@asynctask
def my_task(x, y):
    log.info("I am executing asynchronously :-)")
    log.info("%s + %s = %s" % (x, y, x + y))
    time.sleep(4)
    log.info("And returning...")

def do_async():
    """Call /async and see how pymacaron spawns an asynchronous task"""
    my_task(2, 3)
    log.info("REST endpoint returning now!")
    return ApiPool.helloworld.model.Hello(message='Hello world!')


@asynctask
def my_task_dies(d):
    log.info("I am executing asynchronously, and raising an Exception")
    raise Exception(d['msg'])

def do_async_die():
    my_task_dies({'msg': 'Oh no!'})
    log.info("REST endpoint returning now!")
    return ApiPool.helloworld.model.Hello(message='Hello world!')
