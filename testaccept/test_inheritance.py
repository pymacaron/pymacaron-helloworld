import logging
from pymacaron.test import PyMacaronTestCase


log = logging.getLogger(__name__)


class Test(PyMacaronTestCase):

    def test_inheritance(self):
        j = self.assertCallReturnJson(
            'POST',
            'hello/with/inheritance',
            {
                'question': 'hello?',
            },
            auth="Bearer %s" % self.token
        )
        self.assertEqual(
            j,
            {
                'message': 'You said: hello?',
            }
        )
