import os, json, urllib, cStringIO
def OpenJson(path): 
    json_file = open(path , 'r')
    json_str = json_file.read()
    json_data = json.loads(json_str)
    return json_data

def ExtractLatLongFromGeoJsonForGoogleAPI(d):
	theString = ''

	for i , loc in enumerate(d['features'][0]['geometry']['coordinates']):
		theString += str(loc[1]) 
		theString += ','
		theString += str(loc[0]) 
		theString += '|'
		# if i > 0: 
		# 	pass
	return theString[:-1]

url = 'https://maps.googleapis.com/maps/api/elevation/json?locations='
key = 'YOUR KEYS'

subdir = "LOCAL PATH TO SAVE"
filename = "GEOJSON(elevationFromGoogleAPI.json)"
filepath=os.path.join(subdir,filename)

pts = OpenJson('FILE NAME TO SAVE')
location = ExtractLatLongFromGeoJsonForGoogleAPI(pts)
print location
out = urllib.urlretrieve(url + location + key , filepath)
print 'done'