import logging
from pymacaron.test import PyMacaronTestCase
from pymacaron.config import get_config


log = logging.getLogger(__name__)


class Test(PyMacaronTestCase):

    def setUp(self):
        super(Test, self).setUp()
        self.verify_ssl = False

    def test_async(self):
        j = self.assertCallReturnJson('GET', 'async')
        self.assertTrue(j['message'].startswith('Writing code '))
        code = j['message'].split(' ')[-1]

        # Is this test running locally?
        if self.host != '127.0.0.1':
            return

        # We are running those tests locally, let's check that the code was
        # writen in the uuid file. Note that it may take a short delay for the
        # file to be writen since it is done asynchronously, hence the while
        # loop
        file_path = get_config().uuid_file_path
        count = 0
        found = False
        while not found:
            count += 1
            if count > 5:
                assert 0, "UUID file not writen after 5 seconds..."

            with open(file_path, 'r') as f:
                s = f.read()
                if s == code:
                    found = True
