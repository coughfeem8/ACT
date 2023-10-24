import unittest
from services import shell_printer as sp
from api import amiibo as amiiboApi
from .mock_data import(
    ALL_SERIES,
    ZELDA_SERIES,
    AMIIBO_MEWTWO,
)

class TestShellPrinter(unittest.TestCase):
    '''testing shell commands'''
    def test_list_all_series(self):
        data, count = sp.amiibo_series_to_table(amiiboApi.get_amiibo_series())
        self.assertEqual(ALL_SERIES,data)
        self.assertTrue(count > 0)

    def test_single_series(self):
        data, count = sp.amiibo_characters_to_table(amiiboApi.get_amiibo_single_series('0x010'))
        self.assertEqual(ZELDA_SERIES, data)
        self.assertTrue(count > 0)


    def test_list_single_amiibo(self):
        data, count = sp.amiibo_characters_to_table(amiiboApi.get_amiibo_single('0x1996'))
        print(data)
        print(AMIIBO_MEWTWO)
        self.assertEqual(AMIIBO_MEWTWO,data)
        self.assertTrue(count > 0)

    # failures

    #fail to find amiibo
    # trying to print all amiibos
    # try a bad series.
        
    #setup
    @classmethod
    def setUpClass(self) -> None:
        print('preparing Shell printer test')
              
    @classmethod
    def tearDownClass(self) -> None:
        print('cleaning Shell printer test')

if __name__ == '__main__':
    unittest.main()