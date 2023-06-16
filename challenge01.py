#!/usr/bin/python3 

import requests
import pprint
from datetime import datetime
import reverse_geocoder as rg

ISSURL = "http://api.open-notify.org/iss-now.json"

def main():

    iss = requests.get(ISSURL)
    iss = iss.json()

    long = iss['iss_position']['longitude']
    lat = iss['iss_position']['latitude']
    time = iss['timestamp']

    
    datetime_obj = datetime.fromtimestamp(time)
     
    coords = (lat, long)
    result = rg.search(coords, verbose=False)


    print(f"CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {datetime_obj}")
    print(f"Lon: {long}")
    print(f"Lat: {lat}") 
    print(f"City/Country: {result[0]['name']}/{result[0]['cc']}") 


if __name__ == "__main__":
    main()


