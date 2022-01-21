import os
import logging
from flask import Flask
from pymacaron import API, letsgo


log = logging.getLogger(__name__)

app = Flask(__name__)


def my_error_reporter(title=None, data={}, exception=None):
    """This method receives all errors that should be reported up to
    site admins"""

    log.info(f"Caught exception '{title}' ({exception}) with data: {data}")


def start(port, debug):

    here = os.path.dirname(os.path.realpath(__file__))
    path_apis = os.path.join(here, "apis")

    api = API(
        app,
        port=port,
        debug=debug,
        error_reporter=my_error_reporter,
    )
    api.load_apis(path_apis)
    api.start()


letsgo(__name__, callback=start)
