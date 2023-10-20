import configparser
from typing import Protocol
import requests
from domain.models.amiibo import AmiiboCharacter, GameSeries


class AmiiboApi(Protocol):
    """interface for amiibo api methods"""
    def get_amiibo_series() -> list[GameSeries]:
        ...
    def get_amiibo_single(code: str) -> list[AmiiboCharacter]:
        ...
    def get_amiibo_single_series(code: str) -> list[GameSeries]:
        ...


#* configure this at main instead.
config = configparser.ConfigParser()
config.read('src/config.ini')
BASE_API = config['Apis']['amiibo'];


def get_amiibo_series() -> list[GameSeries]:
    url =  BASE_API+'gameseries'
    try:
        data = requests.get(url).json().get('amiibo')
        if(data):
            return [GameSeries(**i)for i in data]
    except requests.exceptions.RequestException as e:
        print('error getting amiibo series')
        return []

def get_amiibo_single(code: str) -> list[AmiiboCharacter]:
    url =  BASE_API+'amiibo/?character='+code+'&showusage'
    try:
        data = requests.get(url).json().get('amiibo')
        if(data):
            return [AmiiboCharacter(**i) for i in data]
        return data    
    except requests.exceptions.RequestException as e:
        print('error getting amiibo series')
        

def get_amiibo_single_series(code: str) -> list[AmiiboCharacter]:
    url =  BASE_API+'amiibo/?gameseries='+code+'&showusage'
    try:
        data = requests.get(url).json().get('amiibo')
        if(data):
            return [AmiiboCharacter(**i) for i in data]
    except requests.exceptions.RequestException as e:
        print('error getting amiibo series')
        return []


