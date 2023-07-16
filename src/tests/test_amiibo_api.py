import unittest

from api import amiibo

class TestAmiiboApi(unittest.TestCase):
    
    def setUpClass(self) -> None:
        print('''initializing tests for amiibo api wrapper''')
         
    def tearDownClass(self) -> None:
        print('''finished tests for amiibo api wrapper''')

    def setUp(self) -> None:
        print('preparing test')
    
    def tearDown(self) -> None:
        print('cleaning test')


    def test_get_amiibo_series(self):
        self.assertIsNot(amiibo.get_amiibo_series(),{})


unittest.main()