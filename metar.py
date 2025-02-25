#!/usr/bin/python3

#
# A python script to get weather data from ilmailusaa.fi website.
#

import sys
import urllib.request
import json
from datetime import datetime, timezone


# Define remote urls
metartafurl = 'https://ilmailusaa.fi/backend.php?{"mode":"metartaf","radius":"100","points":[{"_area":"4"}]}'
awsmetarurl = 'https://ilmailusaa.fi/backend.php?{"mode":"awsaviation","radius":"100","points":[{"_area":"1"}]}'

# Function to read uriels
def urlfetcher(urli):
    dump = urllib.request.urlopen(urli).read()
    return dump

# Parse returned data
def parsestation(station):
    wxdata = [value['p1'] for value in metarjson.values() if station in value['p1']]
    if not wxdata:
        wxdata = [value['p1'] for value in awsjson.values() if station in value['p1']]
    return wxdata

# Output data
def outputter(wx):
    if not wx:
        print("No data for", station)
    else:
        for data in wx:
            print(data)
    print()


# Fetch and parse jsons
metarjson = json.loads(urlfetcher(metartafurl).decode())
awsjson = json.loads(urlfetcher(awsmetarurl).decode())

# Get UTC time into variable
UTC = datetime.now(timezone.utc).strftime("%b %d %H:%M %Z")

print("\n\tFetched", UTC, "\n")

# If no arguments are given use EFOU <3
if (len(sys.argv) == 1):
    station = "EFOU"
    wx = parsestation(station)
    outputter(wx)
else:
    for i in range(1, len(sys.argv)):
        station = sys.argv[i].upper()
        wx = parsestation(station)
        outputter(wx)
