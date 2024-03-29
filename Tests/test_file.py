import unittest

from Disc.File import *


class TestFile(unittest.TestCase):

    def setUp(self):
        self.file = File("holis", "holis2")

    def test_component_named(self):
        try:
            self.file.component_named("Un archivo inexistente")
        except LookupError, error:
            self.assertEqual("Error you cant search in files!", str(error))


suite = unittest.TestLoader().loadTestsFromTestCase(TestFile)
unittest.TextTestRunner(verbosity=2).run(suite)