import json
import urllib2
import ast

#get ip address
ip = urllib2.urlopen('http://ip.42.pl/raw').read()

#get geo data
URL = "http://www.freegeoip.net/json/" + ip
request= urllib2.urlopen(URL)
result = request.read()
data = json.loads(result)
resultList = data.values()
dump = ast.literal_eval(json.dumps(data))
#print dump

city = dump.get("city")
zip = dump.get("zipcode")
lat = dump.get("latitude")
long = dump.get("longitude")

def getLat():
    print lat
    return lat

def getLong():
    print long
    return long

def getZip():
    print zip
    return zip


