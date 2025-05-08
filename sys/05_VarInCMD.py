#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
#Ejecutarlo en consola como:
# python 05_VarInCMD.py 1545 Disneyland Dr, Anaheim, CA 92802, Estados Unidos

import webbrowser, sys

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
print(address)

webbrowser.open('https://www.google.com/maps/place/'
                + address)
