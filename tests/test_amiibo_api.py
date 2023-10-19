import unittest
from src.api import amiibo

class TestCommands(unittest.TestCase):
    '''testing shell.commands'''
       
    def setUp(self) -> None:
        print('preparing test')

    def tearDown(self) -> None:
        print('cleaning test')


    def test_get_amiibo_series(self):
        self.assertIsNot(amiibo.get_amiibo_series(),{})

if __name__ == '__main__':
    unittest.main()