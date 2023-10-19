## Amiibo Card Tool
python console app that generates artwork and display information about every Amiibo figurine in the market. Useful for NFC cards.

### Features
- request the amiibo series you want to create cards using the Amiibo API
- generates, transforms and set up data to create new set of amiibo card stickers.
- puts new generated cards in a user-specified folder with the aid of vector graphic software such as Inkscape or illustrator & scripts for the given software.
- (future) create UI for previewing vector version and colors for templates.


### How to build
- to run test use the ` poetry run coverage run -m unittest discover`
- to run the application use `poetry run python src/main.py` 