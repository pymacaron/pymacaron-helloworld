from pnt_common.test import PntTest

class Test(PntTest):

    def setUp(self):
        super(Test, self).setUp()

    def test_ping(self):
        self.assertHasPing()

    def test_version(self):
        self.assertHasVersion()

    def test_auth_version(self):
        self.assertHasAuthVersion()

if __name__ == '__main__':
    unittest.main()
