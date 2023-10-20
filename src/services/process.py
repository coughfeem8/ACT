from domain.models import amiibo as a
from abc import ABC, abstractmethod

from prettytable import PrettyTable

class ProcessService(ABC):
    
    @abstractmethod
    def list_amiibo_series():
        """"""




def print_all_series(series:dict) -> None:
    table = PrettyTable()
    if(series):
        table.field_names = ['option','series']
        for row in series:
            table.add_row([row['key'],row['name']])
        print(table)

def print_amiibo_characters(series: dict)-> None:
      table = PrettyTable()
      if(series):
        print(len(series), "Character(s) Found!")
        table.field_names = ['Character','Name','Game Series','Type','Release US']
        for row in series: 
            char = a.AmiiboCharacter(**row)
            table.add_row([char.character,char.name,char.gameSeries,char.type,char.release["na"]])
        print(table)