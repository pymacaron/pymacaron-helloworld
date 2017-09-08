import click
import os
import sys
import logging
from flask import Flask
from klue_microservice import API


log = logging.getLogger(__name__)


@click.command()
@click.option('--port', help="Set server listening port (default: 80)", default=80)
@click.option('--debug/--no-debug', default=True)
def main(port, debug):

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


if __name__ == "__main__":
    main()

if os.path.basename(sys.argv[0]) == 'gunicorn':
    start()
