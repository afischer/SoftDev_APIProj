import location
import json
import urllib2

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

print data
