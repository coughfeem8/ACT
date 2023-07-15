from .docs import STARTUP_DOC
from .core import (
    add_command,
    run_shell
)
from .commands import (
    COMMANDS,
    exit_shell,
    help_shell,
    list_command,
    download_command,
    create_command,
    saved_command,

)
def start_cli() -> None:
    add_command(COMMANDS['exit'],exit_shell)
    add_command(COMMANDS['help'], help_shell)
    add_command(COMMANDS['list'], list_command)
    add_command(COMMANDS['download'], download_command)
    add_command(COMMANDS['create'], create_command)
    add_command(COMMANDS['saved'], saved_command)  
    print(STARTUP_DOC)
    run_shell()