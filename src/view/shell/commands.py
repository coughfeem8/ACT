from .docs import (
    HELP_DOC,
    EXIT_DOC,
    LIST_DOC,
    DOWNLOAD_DOC,
    CREATE_DOC,
    SAVED_DOC
)
from time import sleep
from domain.models import amiibo as a
from prettytable import PrettyTable
from api import amiibo
from services import process


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
def validate_arg(arg:str, variation:list[str]) -> bool:
    return arg.lower().strip() in variation

def help_shell(_: list[str]) -> None:
    print(HELP_DOC)

def exit_shell(_: list[str]) -> None:
    for i in [".", "..", "..."]:
        print(f"  Exiting{i}", end="\r")
        sleep(1)
    print(EXIT_DOC)
    exit(0)

def list_command(args: list[str]) -> None:
    # pull down data to view or search for values.
    #no args
    if len(args)==0:
        process.print_all_series(amiibo.get_amiibo_series())
    #amiibo or series
    elif len(args)==1:
        if validate_arg(args[0],AMIIBO_ARG):
           print(LIST_DOC)
        if validate_arg(args[0],SERIES_ARG):
            process.print_amiibo_characters(amiibo.get_amiibo_series(args[1]))
    #amiibo or series w code
    elif len(args)==2:
        if validate_arg(args[0],AMIIBO_ARG):
            process.print_amiibo_characters(amiibo.get_amiibo_single(args[1]))
        if validate_arg(args[0],SERIES_ARG):
            process.print_amiibo_characters(amiibo.get_amiibo_single_series(args[1]))
    else:
        print(LIST_DOC)
        
def download_command(args: list[str]) -> None:
    print('download command')
    # similar to list but this process will create the entries and store it locally on the application.
    #no args
    if len(args)==0: #? ask if they are sure to download everything
        print('download everything')
    #amiibo or series
    elif len(args)==1:
        if validate_arg(args[0],AMIIBO_ARG): #? ask if they are sure to download everything
          print("download all amiibos")
        if validate_arg(args[0],SERIES_ARG): #? ask if they are sure to download everything
          print('download everything by series')
    #amiibo or series w code
    elif len(args)==2:
        if validate_arg(args[0],AMIIBO_ARG):
           print(f'download data for character {args[1]}')
        if validate_arg(args[0],SERIES_ARG):
          print(f'download data for series {args[1]}')
    else:
        print(DOWNLOAD_DOC)

def create_command(args: list[str]) -> None:
    print('create command')
    # request  either to render all the locally stored items
    if len(args)==0: #? ask if they are sure to download everything
        print('create all saved amiibos.')
    #amiibo or series
    elif len(args)==1:
        print("provide code for the series or character")
    elif len(args)==2:
        if validate_arg(args[0],AMIIBO_ARG): #? ask if they are sure to download everything
          print(f'render amiibo(s) for character {args[1]}')
        if validate_arg(args[0],SERIES_ARG): #? ask if they are sure to download everything
          print(f'render amiibo(s) for series {args[1]} ')
    else:
        print(CREATE_DOC)
    #amiibo or series w code

def saved_command(args: list[str]) -> None:
    print('saved command')
    if not len(args) == 0:
        print(SAVED_DOC)
        return
    #display all locally stored amiibo data
    print('these are the amiibos locally stored.')