from .docs import (HELP_DOC, EXIT_DOC, LIST_DOC)
from time import sleep
from domain.models.amiibo import AmiiboCharacter
from prettytable import PrettyTable
from api import get_amiibo_series, get_amiibo_single, get_amiibo_single_series


AMIIBO_ARG = ['amiibo','a']
SERIES_ARG = ['series','s']
COMMANDS = {
    'list':['list','l'],
    'download':['download','d'],
    'create':['create','c'],
    'saved':['saved','s'],
    'help':['help', 'h'],
    'exit': ['exit']
}

def help_shell(_: list[str]) -> None:
    print(HELP_DOC)

def exit_shell(_: list[str]) -> None:
    for i in [".", "..", "..."]:
        print(f"  Exiting{i}", end="\r")
        sleep(1)
    print(EXIT_DOC)
    exit(0)

def list_command(args: list[str]) -> None:
    print(args)
    #no args
    if len(args)==0:
        print_all_series()
    #amiibo or series
    elif len(args)==1:
        if validate_arg(args[0],AMIIBO_ARG):
           print(LIST_DOC)
        if validate_arg(args[0],SERIES_ARG):
           print_amiibo_characters(get_amiibo_series(args[1]))
    #amiibo or series w code
    elif len(args)==2:
        if validate_arg(args[0],AMIIBO_ARG):
           print_amiibo_characters(get_amiibo_single(args[1]))
        if validate_arg(args[0],SERIES_ARG):
           print_amiibo_characters(get_amiibo_series(args[1]))
    else:
        print(LIST_DOC)
    
    
        
def download_command(args: list[str]) -> None:
    print('download command')

def create_command(args: list[str]) -> None:
    print('create command')

def saved_command(args: list[str]) -> None:
    print('saved command')


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
            char = AmiiboCharacter(**row)
            table.add_row([char.character,char.name,char.gameSeries,char.type,char.release["na"]])
        print(table)

def validate_arg(arg:str, variation:list[str]) -> bool:
    return arg.lower().strip() in variation