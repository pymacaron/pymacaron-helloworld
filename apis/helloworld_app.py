# This is an auto-generated file - DO NOT EDIT!!!
from flask_cors import cross_origin
from typing import Optional
from pydantic import BaseModel
from pymacaron.endpoint import pymacaron_flask_endpoint
from pymacaron.log import pymlogger


log = pymlogger(__name__)


def load_endpoints(app=None, error_callback=None):
    from pymacaron import apipool


    from helloworld.api import do_hello as f_helloworld_api_do_hello

    from helloworld.api import do_hello as f_helloworld_api_do_hello_via_requires_auth
    from pymacaron.auth import requires_auth
    f_helloworld_api_do_hello_via_requires_auth = requires_auth(f_helloworld_api_do_hello_via_requires_auth)

    from helloworld.api import do_hello_with_inheritance as f_helloworld_api_do_hello_with_inheritance_via_requires_auth
    from pymacaron.auth import requires_auth
    f_helloworld_api_do_hello_with_inheritance_via_requires_auth = requires_auth(f_helloworld_api_do_hello_with_inheritance_via_requires_auth)

    from helloworld.api import do_crash as f_helloworld_api_do_crash

    from helloworld.api import do_async as f_helloworld_api_do_async

    from helloworld.api import do_async_die as f_helloworld_api_do_async_die

    @app.route("/hello", methods=["GET"])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def endpoint_get__hello():
        return pymacaron_flask_endpoint(
            api_name="helloworld",
            f=f_helloworld_api_do_hello,
            path_args={
            },
            form_args={
            },
            body_model_name=None,
            query_model=None,
            produces="application/json",
            result_models=[
                apipool.helloworld.Hello,
            ],
            error_callback=error_callback,
        )
    log.info("Binding [helloworld] GET /hello ==> helloworld.api.do_hello")


    @app.route("/hello/with/auth", methods=["GET"])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def endpoint_get__hello_with_auth():
        return pymacaron_flask_endpoint(
            api_name="helloworld",
            f=f_helloworld_api_do_hello_via_requires_auth,
            path_args={
            },
            form_args={
            },
            body_model_name=None,
            query_model=None,
            produces="application/json",
            result_models=[
                apipool.helloworld.Hello,
            ],
            error_callback=error_callback,
        )
    log.info("Binding [helloworld] GET /hello/with/auth ==> helloworld.api.do_hello")


    @app.route("/hello/with/inheritance", methods=["POST"])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def endpoint_post__hello_with_inheritance():
        return pymacaron_flask_endpoint(
            api_name="helloworld",
            f=f_helloworld_api_do_hello_with_inheritance_via_requires_auth,
            path_args={
            },
            form_args={
            },
            body_model_name="Question",
            query_model=None,
            produces="application/json",
            result_models=[
                apipool.helloworld.Hello,
            ],
            error_callback=error_callback,
        )
    log.info("Binding [helloworld] POST /hello/with/inheritance ==> helloworld.api.do_hello_with_inheritance")


    @app.route("/die", methods=["GET"])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def endpoint_get__die():
        return pymacaron_flask_endpoint(
            api_name="helloworld",
            f=f_helloworld_api_do_crash,
            path_args={
            },
            form_args={
            },
            body_model_name=None,
            query_model=None,
            produces="application/json",
            result_models=[
                apipool.helloworld.Hello,
            ],
            error_callback=error_callback,
        )
    log.info("Binding [helloworld] GET /die ==> helloworld.api.do_crash")


    @app.route("/async", methods=["GET"])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def endpoint_get__async():
        return pymacaron_flask_endpoint(
            api_name="helloworld",
            f=f_helloworld_api_do_async,
            path_args={
            },
            form_args={
            },
            body_model_name=None,
            query_model=None,
            produces="application/json",
            result_models=[
                apipool.helloworld.Hello,
            ],
            error_callback=error_callback,
        )
    log.info("Binding [helloworld] GET /async ==> helloworld.api.do_async")


    @app.route("/asyncdie", methods=["GET"])
    @cross_origin(headers=["Content-Type", "Authorization"])
    def endpoint_get__asyncdie():
        return pymacaron_flask_endpoint(
            api_name="helloworld",
            f=f_helloworld_api_do_async_die,
            path_args={
            },
            form_args={
            },
            body_model_name=None,
            query_model=None,
            produces="application/json",
            result_models=[
                apipool.helloworld.Hello,
            ],
            error_callback=error_callback,
        )
    log.info("Binding [helloworld] GET /asyncdie ==> helloworld.api.do_async_die")
