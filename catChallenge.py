#!/usr/bin/env python3

import requests
import pprint
import json 

URL = "https://cat-fact.herokuapp.com/facts"
 
def main():
    response = requests.get(URL).json()

    for x in response:
        int i = 0 
        cat_fact = response[i]['text']
        
        print(f"Cat fact: {cat_fact}")
        
if __name__ == "__main__":
    main()
