from .docs import STARTUP_DOC
from .core import (
    add_command,
    run_shell
)
from .commands import (
    exit_shell,
    help_shell,
    list_command,
    download_command,
    create_command,
    saved_command
)


def start_cli() -> None:
    
    add_command(['exit'],exit_shell)
    add_command(['help', 'h'], help_shell)
    add_command(['list','l'], list_command)
    add_command(['download','d'], download_command)
    add_command(['create','c'], create_command)
    add_command(['saved','s'], saved_command)  
    print(STARTUP_DOC)
    run_shell()