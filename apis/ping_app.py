# This is an auto-generated file - DO NOT EDIT!!!
from flask_cors import cross_origin
from typing import Optional
from pydantic import BaseModel
from pymacaron.endpoint import pymacaron_flask_endpoint
from pymacaron.log import pymlogger


log = pymlogger(__name__)


def load_endpoints(app=None, error_callback=None):
    from pymacaron import apipool


    from pymacaron.api import do_ping as f_pymacaron_api_do_ping

    from pymacaron.api import do_version as f_pymacaron_api_do_version

    from pymacaron.api import do_version as f_pymacaron_api_do_version_via_requires_auth
    from pymacaron.auth import requires_auth
    f_pymacaron_api_do_version_via_requires_auth = requires_auth(f_pymacaron_api_do_version_via_requires_auth)

    @app.route("/ping", methods=["GET"])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def endpoint_get__ping():
        return pymacaron_flask_endpoint(
            api_name="ping",
            f=f_pymacaron_api_do_ping,
            path_args={
            },
            form_args={
            },
            body_model_name=None,
            query_model=None,
            produces="application/json",
            result_models=[
                apipool.ping.Ok,
                apipool.ping.Error,
            ],
            error_callback=error_callback,
        )
    log.info("Binding [ping] GET /ping ==> pymacaron.api.do_ping")


    @app.route("/version", methods=["GET"])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def endpoint_get__version():
        return pymacaron_flask_endpoint(
            api_name="ping",
            f=f_pymacaron_api_do_version,
            path_args={
            },
            form_args={
            },
            body_model_name=None,
            query_model=None,
            produces="application/json",
            result_models=[
                apipool.ping.Version,
                apipool.ping.Error,
            ],
            error_callback=error_callback,
        )
    log.info("Binding [ping] GET /version ==> pymacaron.api.do_version")


    @app.route("/auth/version", methods=["GET"])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def endpoint_get__auth_version():
        return pymacaron_flask_endpoint(
            api_name="ping",
            f=f_pymacaron_api_do_version_via_requires_auth,
            path_args={
            },
            form_args={
            },
            body_model_name=None,
            query_model=None,
            produces="application/json",
            result_models=[
                apipool.ping.Version,
                apipool.ping.Error,
            ],
            error_callback=error_callback,
        )
    log.info("Binding [ping] GET /auth/version ==> pymacaron.api.do_version")
