import logging
from pymacaron.test import PyMacaronTestCase


log = logging.getLogger(__name__)


class Test(PyMacaronTestCase):

    def test_auth(self):
        j = self.assertCallReturnJson(
            'GET',
            'hello/with/auth',
            auth="Bearer %s" % self.token
        )
        self.assertTrue('message' in j)
