import json
from types import SimpleNamespace
import requests
import constants
from prettytable import PrettyTable
from amiibo import AmiiboCharacter


### state
selected_amiibo_series = ''

### request
def get_amiibo_series():
    url =  constants.BASE_API+'gameseries'
    try:
        return requests.get(url).json().get('amiibo')
    except requests.exceptions.RequestException as e:
        print('error getting amiibo series')
        return False

def get_amiibo_single_series(code):
    url =  constants.BASE_API+'amiibo/?gameseries='+code+'&showusage'
    try:
        return requests.get(url).json().get('amiibo') 
    except requests.exceptions.RequestException as e:
        print('error getting amiibo series')
        return False


### prints
def print_amiibo_options():
    table = PrettyTable()
    series = get_amiibo_series()
    if(series):
        table.field_names = ['option','series']
        for row in series:
            table.add_row([row['key'],row['name']])
        print(table)

def  print_amiibo_series_data(code):
    print(code)
    table = PrettyTable()
    series = get_amiibo_single_series(code)
    if(series):
        print(len(series), "Character(s) Found!")
        table.field_names = ['Character','Name','Game Series','Type','Release US']
        for row in series:
            
            char = AmiiboCharacter(**row)
            table.add_row([char.character,char.name,char.gameSeries,char.type,char.release["na"]])
        print(table)
if __name__ == "__main__":
    print('welcome to ACT')
    print('provide the series of amiibos to generate cards for:')
    print_amiibo_options()
    selected_amiibo_series = input('option:')
    if(selected_amiibo_series != ''):
        print_amiibo_series_data(selected_amiibo_series)
    else:
        print('not a valid option')
    
    
