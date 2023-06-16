#!/usr/bin/python3

import requests

DATEURL = "http://date.jsontest.com/"
IPURL = "http://ip.jsontest.com/"
POSTURL = "http://validate.jsontest.com/"

def main():
    timereq = requests.get(DATEURL).json()
    time = timereq['time']


