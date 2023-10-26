import unittest
from services import shell_printer as sp
from api import amiibo as amiiboApi
from .mock_data import (
    create_character_series_data,
    create_game_series_data,
    create_single_character_data
)

class TestShellPrinter(unittest.TestCase):
    '''testing shell commands'''
    def test_list_all_series(self):
        data, count = sp.amiibo_series_to_table(self.SERIES_DATA)
   
        self.assertTrue(count > 0)

    def test_single_series(self):
        data, count = sp.amiibo_characters_to_table(self.ZELDA_SERIES)

        self.assertTrue(count > 0)

    def test_list_single_amiibo(self):
        data, count = sp.amiibo_characters_to_table(self.AMIIBO_MEWTWO)  
        self.assertTrue(count > 0)

    # failures

    #fail to find amiibo
    # trying to print all amiibos
    # try a bad series.
        
    #setup
    @classmethod
    def setUpClass(self) -> None:
        print('preparing Shell printer test')
        self.SERIES_DATA = create_game_series_data()
        self.AMIIBO_MEWTWO = create_single_character_data()
        self.ZELDA_SERIES = create_character_series_data()
              
    @classmethod
    def tearDownClass(self) -> None:
        print('cleaning Shell printer test')

if __name__ == '__main__':
    unittest.main()