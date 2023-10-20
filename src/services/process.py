from domain.models import amiibo as a

from prettytable import PrettyTable

def print_all_series(series:list[a.GameSeries]) -> None:
    table = PrettyTable()
    if(series):
        table.field_names = ['option','series']
        for row in series:
            table.add_row([row.key,row.name])
        print(table)

def print_amiibo_characters(series: list[a.AmiiboCharacter])-> None:
      table = PrettyTable()
      if(series):
        print(len(series), "Character(s) Found!")
        table.field_names = ['Character','Name','Game Series','Type','Release US']
        for char in series: 
            table.add_row([char.character,char.name,char.gameSeries,char.type,char.release["na"]])
        print(table)