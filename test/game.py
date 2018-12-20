class TestPackages(unittest.TestCase):
    def setUp(self):
        """Before unittest"""
        pwd = os.path.dirname(__file__)
        filename = "%s/%s" % (pwd, "packages.cache")
        self.__allpackages = loadPkgInfo(filename, False, True)

    def test_summary(self):
        """ test summary properties"""
        self.assertEqual(True, True)
