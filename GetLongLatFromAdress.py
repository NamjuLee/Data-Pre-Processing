import pandas as pd
from geopy.geocoders import Nominatim
def GetPandasFromFileCSV(path):
    return pd.read_csv(path, delimiter=',')
def SavePandasToCSV(d, path):
	d.to_csv(path)
	return "done!!"
def GetGeoCodeFromAdress(address):
	theGeo = []
	theAdress = []
	geolocator = Nominatim()
	count = 1;
	total = len(address)
	for a in address:
		if(str(a) != "null"):
			try:
				location = geolocator.geocode(a)
				theAdress.append(location.address)
				theGeo.append((location.latitude, location.longitude))
				print location.address
				print location.latitude, location.longitude
			except:
				theAdress.append("null")
				theGeo.append('null')
		print (float(count) / float(total)) * 100 , " % ..."
		count+=1
	return theGeo, theAdress
def GetConcatenateAdress(adress , theZip):
	result = [];
	for i in range(len(adress)):
		# print adress[i]
		if(str(adress[i]) != "nan"):
			result.append(str(adress[i]) + " Boston MA " )# + str(theZip[i]))
		else:
			result.append('null')
	return result

d = GetPandasFromFileCSV('YOUR CSV FILE')
theAdress = d['Address'].tolist();
theZip = d['ZIP'].tolist();

adress=GetConcatenateAdress(theAdress, theZip)
theGeo, theAdress=GetGeoCodeFromAdress(adress)

df = pd.DataFrame();
df['pos'] = theGeo
df['fullAdress'] = theAdress
SavePandasToCSV(df, "THE NEW FILE")
