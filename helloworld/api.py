import logging
from uuid import uuid4
from pymacaron_async import asynctask
from pymacaron.config import get_config
from pymacaron_core.models import PyMacaronModel
from pymacaron_core.models import get_model


log = logging.getLogger(__name__)


def do_hello():
    """Replies to a call to /hello"""
    return get_model('Hello')(message='Hello world!')


#
# The following methods are for educational purpose only.
# Remove them when cloning helloworld to bootstrap your own microservice.
#

def do_crash():
    """Call /die and see how pymacaron handles an exception"""
    raise Exception("OH! NO! I JUST DIED!!")


@asynctask()
def my_task_async(a, b, c, d, o, dict_arg=None):
    log.info("I am executing asynchronously :-)")

    assert a == 1
    assert b == '2'
    assert c == {'3': '4'}
    assert d == [5, 6, 7]
    assert isinstance(o, PyMacaronModel)
    assert isinstance(dict_arg, PyMacaronModel)
    assert dict_arg.code == o.code

    # write the unique code to the uuid file
    file_path = get_config().uuid_file_path
    with open(file_path, 'w') as f:
        log.info("Writing uuid code %s to %s" % (o.code, file_path))
        f.write(o.code)


def do_async():
    """Call /async and see how pymacaron spawns an asynchronous task"""
    # Generate a unique code
    code = get_model('Code')(
        code=str(uuid4()),
    )

    # Arguments to asynchronous methods may be python primitives or PyMacaron
    # models, passed as list or dictionary arguments
    my_task_async(1, '2', {'3': '4'}, [5, 6, 7], code, dict_arg=code)

    log.info("REST endpoint returning now!")
    return get_model('Hello')(message='Writing code %s' % code.code)


@asynctask()
def my_task_dies(d):
    log.info("I am executing asynchronously, and raising an Exception")
    raise Exception(d['msg'])


def do_async_die():
    my_task_dies({'msg': 'Oh no!'})
    log.info("REST endpoint returning now!")
    return get_model('Hello')(message='Hello world!')
