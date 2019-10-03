import logging
from pymacaron.test import PyMacaronTestCase


log = logging.getLogger(__name__)


class Test(PyMacaronTestCase):

    def setUp(self):
        super(Test, self).setUp()
        self.verify_ssl = False

    def test_ping(self):
        self.assertHasPing()

    def test_version(self):
        self.assertHasVersion(verify_ssl=self.verify_ssl)

    def test_auth_version(self):
        self.assertHasAuthVersion(verify_ssl=self.verify_ssl)
