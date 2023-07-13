import requests

BASE_API = 'https://www.amiiboapi.com/api/'

def get_amiibo_series() -> dict:
    url =  BASE_API+'gameseries'
    try:
        return requests.get(url).json().get('amiibo')
    except requests.exceptions.RequestException as e:
        print('error getting amiibo series')

def get_amiibo_single_series(code:str) -> dict:
    url =  BASE_API+'amiibo/?gameseries='+code+'&showusage'
    try:
        return requests.get(url).json().get('amiibo') 
    except requests.exceptions.RequestException as e:
        print('error getting amiibo series')