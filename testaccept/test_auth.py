import logging
from pymacaron.test import PyMacaronTestCase
from pymacaron.auth import generate_token


log = logging.getLogger(__name__)


class Test(PyMacaronTestCase):

    def test_auth(self):
        token = generate_token(user_id='test-jwt-token')
        j = self.assertCallReturnJson(
            'GET',
            'hello/with/auth',
            auth="Bearer %s" % token
        )
        self.assertTrue('message' in j)
