from colorama import Fore as f

STARTUP_DOC = f"""
{f.YELLOW}ACT CLI
LICENCIE: MIT
Language: {f.CYAN}Python3.10{f.YELLOW}
Description: A tool to keep track and create custom
amiibo card artwork using the Amiibo API and templates.
"""
HELP_DOC = """
    Usage: <command> <search> [<code>]
        command: either list, download, create, saved
        search: amiibo or series
        code: id for series or amiibo being searched the name works for amiibo too
"""


LIST_DOC = f"""
Usage:
     Usage: <command> <search> <code>
        description: retrieve list of amiibos or series of amiibos given the search criteria.
        search: amiibo or series
        code: id for series or amiibo being searched the name works for amiibo too
"""
DOWNLOAD_DOC = f"""
Usage:
     Usage: <command> <search> <code>
        description: same as list, but also stores the resulting into a local database with images and qr codes.
        search: amiibo or series
        code: id for series or amiibo being searched the name works for amiibo too
"""
CREATRE_DOC = f"""
Usage:
     Usage: <command> <search>? <code>
        description: triggers process to generate artwork for the given process
        search: amiibo or series
        code: id for series or amiibo being searched the name works for amiibo too
"""

SAVED_DOC = f"""
Usage:
     Usage: <command> <search>? <code>
        description: request list of locally stored metadata for ACT
        search: amiibo or series
        code: id for series or amiibo being searched the name works for amiibo too
"""
EXIT_DOC = f"""{f.YELLOW}
    Thanks for using ACT
"""