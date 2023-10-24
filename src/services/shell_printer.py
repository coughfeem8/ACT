from domain.models import amiibo as a
from typing import Tuple
from prettytable import PrettyTable

def amiibo_series_to_table(series:list[a.GameSeries]) -> Tuple[PrettyTable, int]:
    table = PrettyTable()
    length = 0
    if(series):
        length = len(series)
        table.field_names = ['option','series']
        for row in series:
            table.add_row([row.key,row.name])
    return table, length

def amiibo_characters_to_table(characters: list[a.AmiiboCharacter])-> Tuple[PrettyTable, int]:
    table = PrettyTable()
    length = 0
    if(characters):
        length = len(characters)
        table.field_names = ['Character','Name','Game Series','Type','Release US']
        for char in characters: 
            table.add_row([char.character,char.name,char.gameSeries,char.type,char.release["na"]])
    return table, length