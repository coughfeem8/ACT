from domain.models.amiibo import AmiiboCharacter, GameSeries
from typing import List
import json

MOCK_DATA_PATH = 'src/tests/data/'

def create_game_series_data()-> List[GameSeries]:
    f = open(MOCK_DATA_PATH+'game_series.json')
    data = json.load(f).get('amiibo')
    f.close()
    return [GameSeries(**i) for i in data];

def create_character_series_data()-> List[AmiiboCharacter]:
    f = open(MOCK_DATA_PATH+'zelda_series.json')
    data = json.load(f).get('amiibo')
    f.close()
    return [AmiiboCharacter(**i) for i in data];

def create_single_character_data()-> List[AmiiboCharacter]:
    f = open(MOCK_DATA_PATH+'mewtwo.json')
    data = json.load(f).get('amiibo')
    f.close()
    return [AmiiboCharacter(**i) for i in data];