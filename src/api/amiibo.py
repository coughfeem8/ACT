import configparser
import requests

#* configure this at main instead.
config = configparser.ConfigParser()
config.read('src/config.ini')
BASE_API = config['Apis']['amiibo'];


def get_amiibo_series() -> dict:
    url =  BASE_API+'gameseries'
    try:
        return requests.get(url).json().get('amiibo')
    except requests.exceptions.RequestException as e:
        print('error getting amiibo series')

def get_amiibo_single(code: str) -> dict:
    url =  BASE_API+'amiibo/?character='+code+'&showusage'
    try:
        return requests.get(url).json().get('amiibo') 
    except requests.exceptions.RequestException as e:
        print('error getting amiibo series')

def get_amiibo_single_series(code: str) -> dict:
    url =  BASE_API+'amiibo/?gameseries='+code+'&showusage'
    try:
        return requests.get(url).json().get('amiibo') 
    except requests.exceptions.RequestException as e:
        print('error getting amiibo series')


