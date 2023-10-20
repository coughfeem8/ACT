from view.shell import cli
from view.UI import gui
import argparse

def main() -> None:

    argParser = argparse.ArgumentParser()
    argParser.add_argument("-m", "--mode",type=str, help="UI Mode")
    args = argParser.parse_args()

    if(args.mode =='gui'):
        gui.start();
    else:
        cli.start()
    
    
if __name__ == "__main__":
    main()
    
