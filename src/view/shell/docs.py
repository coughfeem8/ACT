from colorama import Fore as f

STARTUP_DOC = f"""
{f.YELLOW}ACT CLI
LICENCIE: MIT
Language: {f.CYAN}Python3.10{f.YELLOW}
Description: A tool to keep track and create custom
amiibo card artwork using the Amiibo API and templates.
"""

HELP_DOC = """
Usage:
To list amiibo data:
    list amiibo -c <code>
    list series
To download metadata artwork and qr codes:
    download <amiibo|series> -c <code>
To create cards:
    create amiibo -c <code>
To list saved data for amiibos and series:
    saved 
Get Help:
    help
Exit:
    exit
"""


LIST_DOC = f"""
Usage:
    {f.YELLOW}<list|l> <<amiibo|a>|<series|s>> (<code|c> .*)?
    {f.WHITE}l : list series
    list :list series
    list series
    l series
    l s
    list series code <code>:list specific amiibo series
    list series c <code> l
    list amiibo -c <code>
"""
EXIT_DOC = f"""{f.YELLOW}
    Thanks for using ACT
"""