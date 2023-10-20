## Amiibo Card Tool
python app that generates artwork and displays information about every Amiibo figurine in the market. Useful for NFC cards.

### description
I've seen the use of nfc cards to use as amiibo but the idea of just having the same white background with the name of the amiibo is not enough for me. There's also online options that have pre-made cards but still a bit generic. So i've decided to create the art work myself. Ideally i would add the art by hand, but honestly i want to do it programmatically just for fun. I just started by creating a good template and filling it with as much info in an aesthetic manner.

Here are a few examples:

![smash back](./assets/smash%20back%20card%20link.png)

![smash front](./assets/smash%20front%20card%20link.png)

![Zelda back](./assets/zelda%20back%20card%20link.png)

![Zelda front](./assets/zelda%20front%20card%20Link.png)

The data is being pulled off from [amiibo api](https://amiiboapi.com/). the original design was created using Figma then translated to Illustrator.
#### template
This is the data that get added to the format
- game series
- figure name
- figure image
- release date
- amiibo series logo
- amiibo qr image
- head and tail of amiibo data
- amiibo usage

info not included in the program
- nfc card data,
    - this should be taken from your own amiibos, i'm not adding a way to add them.  

### Features
- request the amiibo series you want to create cards using the Amiibo API
- generates, transforms and set up data to create new set of amiibo card stickers.
- puts new generated cards in a user-specified folder with the aid of vector graphic software such as Inkscape or Illustrator & scripts for the given software.
- (future) create UI for previewing vector version and colors for templates.

### How to run 
- to run the application use `poetry run python src/main.py` 
### How to test
- to run test use the `poetry run coverage run -m unittest discover -s ./src`
- to see coverage report use  `poetry run coverage report`
- to visualize the coverage report in a browser use `poetry run coverage html`