import os
import sys
import logging
from flask import Flask
from klue_microservice import API, letsgo


log = logging.getLogger(__name__)


def start(port, debug):

    here = os.path.dirname(os.path.realpath(__file__))
    path_apis = os.path.join(here, "apis")

    app = Flask(__name__)
    api = API(
        app,
        port=port,
        debug=debug,
        jwt_secret=os.environ.get("KLUE_JWT_SECRET"),
        jwt_audience=os.environ.get("KLUE_JWT_AUDIENCE"),
    )
    api.load_apis(path_apis)
    api.start(serve="helloworld")


letsgo(__name__, callback=start)
