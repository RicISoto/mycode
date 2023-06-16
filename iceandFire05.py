#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"
#AOIF_HOUS = "https://www.anapioficeandfire.com/api/houses/"
#AOIF_BOOK = "https://www.anapioficeandfire.com/api/books/"
def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )
        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)
       
        #housresp = requests.get(AOIF_HOUS + got_charToLookup)
        
        #bookresp = requests.get(AOIF_BOOK + got_charToLookup) 
        ## Decode the response
        got_dj = gotresp.json()
        housresp = requests.get(got_dj.get("allegiances"))
        got_house = housresp.json()

        for i in got_house:
            print(i)

        #got_house = houseresp.json()

        print(f"You chose: {got_dj['aliases']}")

        #pprint.pprint(got_dj)
        #pprint.pprint(got_house)
if __name__ == "__main__":
        main()

