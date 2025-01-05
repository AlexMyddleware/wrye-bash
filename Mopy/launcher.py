# launcher.py (place this in the Mopy directory)
import sys
from bash import bash
from argparse import Namespace

if __name__ == '__main__':
    # Create a Namespace object with default values
    opts = Namespace(
        language=None,  # Default language
        restore=False,
        filename=None,
        userPath=None,
        genHtml=None,
        quietquit=False,
        uac=False,
        noUac=False,
        backup=False,
        unsupported=False,
        oblivionPath=None,
        personalPath=None,
        localAppDataPath=None,
    )
    bash.main(opts)