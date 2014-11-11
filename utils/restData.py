import location
import json
import urllib2
import ast

# API stuffs
URL = "http://api.v3.factual.com/t/restaurants-us?geo={\"$point\":[%s,%s]}&KEY=q5Ieq2lbPoLh5vnJjmIOqFEktsghyQBTmIgWewgk"

# Location Data
lat = location.getLat()
long = location.getLong()

# URL with correct lat/long
locURL = URL%(lat,long)
print locURL

# Lets get some dataaaaaa
request = urllib2.urlopen(locURL)
result = request.read()

# JSONify that shiz
data = json.loads(result)
rList = data.get("response").get("data")

L = []

for item in rList:
    L = L + [item.get("name"), item.get("website"), item.get("price"), item.get("rating")]

print L


def getNearby():
    return L

def getPriceLevel(price):
    ans = []
    for item in L
    if item[2] == price:
        ans = ans + item
    return ans
