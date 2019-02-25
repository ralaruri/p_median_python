import pandas as pd
import numpy as np
import googlemaps
import gmaps

API_KEY = 'YOUR API KEY'
gm = googlemaps.Client(key=API_KEY)

data = pd.read_csv('/Users/Ramzi/Dropbox/GGS 675/Location Science Project/VA_Tesla_Current2.csv', low_memory=False, index_col = 'id')
data = data.fillna('') # fill empty entries with ''
print(list(data)) # print Variable
print(data.head())

[maxRow,maxCol] = data.shape
print(maxRow,maxCol)

def Geocode(query):
    # do geocoding
    try:
        geocode_result = gm.geocode(query)[0]       
        latitude = geocode_result['geometry']['location']['lat']
        longitude = geocode_result['geometry']['location']['lng']
        return latitude,longitude
    except IndexError:
        return 0
        
def GeocodeStreetLocationCity(data):
    lat=[]                            # initialize latitude list
    lng=[]                            # initialize longitude list
    start = data.index[0]             # start from the first data
    end = data.index[maxRow-1]        # end at maximum number of row
    for i in range(start,end+1,1):    # iterate all rows in the data
        isSuccess=True                # initial Boolean flag
        query = data.address[i] + ' ' + data.name[i] + ' ' + data.city[i]  # try set up our query street-location-city 
        result=Geocode(query)
        if result==0:         # if not successful,
            query = data.address[i] + ' ' + data.city[i]                     # try set up another query location-city
            result=Geocode(query)
            if result==0:     # if still not successful,
                query =  data.name[i] + ' ' + data.city[i]                  # try set up another query street-city
                result=Geocode(query)
                if Geocode(query)==0: # if still not successful,
                    isSuccess=False                                           # mark as unsuccessful
                    print(i, 'is failed')
                else:
                    print(i, result)
            else:
                print(i, result)
        else:
            print(i, result)
        if isSuccess==True:           # if geocoding is successful,
            # store the results
            lat.append(result[0])     # latitude
            lng.append(result[1])     # longitude
    return lat,lng

[lat,lng]=GeocodeStreetLocationCity(data)

df = pd.DataFrame(
    {'latitude': lat,
     'longitude': lng
    })
df.to_csv('locations2.csv')
print('saved geocoded locations to "locations2.csv"')


data1 = pd.read_csv('/Users/Ramzi/Dropbox/GGS 675/Location Science Project/VA_Tesla_Current2.csv', low_memory=False, index_col = 'id')

data2 = pd.read_csv('/Users/Ramzi/Dropbox/GGS 675/Location Science Project/locations2.csv', low_memory=False, index_col = 'id')

result = pd.concat([data1, data2], axis =1)

print(result)


result.to_csv('/Users/Ramzi/Dropbox/GGS 675/Location Science Project/VA_Tesla_Geolocated2.csv')

