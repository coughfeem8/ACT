from api import get_amiibo_series, get_amiibo_single_series
from domain.models.amiibo import AmiiboCharacter
from prettytable import PrettyTable

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

def run_shell() -> None:
    selected_amiibo_series = ''
    print('welcome to ACT')
    print('provide the series of amiibos to generate cards for:')
    print_amiibo_options()
    selected_amiibo_series = input('option:')
    if(selected_amiibo_series != ''):
        print_amiibo_series_data(selected_amiibo_series)
    else:
        print('not a valid option')