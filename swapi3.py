#!/usr/bin/env python3
"""Alta3 Research
   Star Wars API HTTP response parsing"""

# pprint makes dictionaries a lot more human readable
from pprint import pprint

# requests is used to send HTTP requests (get it?)
import requests

#URL = "https://swapi.dev/luke/force"      # Comment out this line
URL= "https://swapi.dev/api/people/4/"     # Uncomment this line
URL1= "https://swapi.dev/api/films/1/" 
URL2= "https://swapi.dev/api/starships/13/"

def main():
    """sending GET request, checking response"""

    # SWAPI response is stored in "resp" object
    resp= requests.get(URL)
    resp1= requests.get(URL1)
    resp2= requests.get(URL2)
    # check to see if the status is anything other than what we want, a 200 OK
    if resp.status_code == 200:
        # convert the JSON content of the response into a python dictionary
        vader= resp.json()
        film= resp1.json()
        ship= resp2.json()

        print(f"{vader['name']} was born in the year {vader['birth_year']}. His eyes are {vader['eye_color']} and his hair color is {vader['hair_color']}")

        print(f"He first appeared in the movie {film['title']} and could be found flying around in his {ship['name']}")

        #pprint(vader)

    else:
        print("That is not a valid URL.")

if __name__ == "__main__":
    main()

