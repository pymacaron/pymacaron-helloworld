import logging
from pymacaron.test import PyMacaronTestCase
from pymacaron.auth import generate_token


log = logging.getLogger(__name__)


class Test(PyMacaronTestCase):

    def test_inheritance(self):
        token = generate_token(user_id='test-jwt-token')
        j = self.assertCallReturnJson(
            'POST',
            'hello/with/inheritance',
            {
                'question': 'hello?',
            },
            auth="Bearer %s" % token
        )
        self.assertEqual(
            j,
            {
                'message': 'You said: hello?',
            }
        )
