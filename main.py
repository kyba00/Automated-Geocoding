import re
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import regex
import requests
import json

def main():

    PCURL = 'https://www.richmondhill.ca/en/things-to-do/Things-to-Do-Splash-Pads.aspx#Bridgeview-Park-Closed'
    pcres = requests.get(PCURL)
    contents = pcres.content
    soup = BeautifulSoup(contents,features="html.parser")
    text = soup.get_text()
    Postal = re.findall("\w\d\w\s\d\w\d",text)
    exist_count = Postal.count('L4B 3P4')
    if exist_count > 0:
        Postal.remove('L4B 3P4')
    latitude = []
    longitude = []

    for p in Postal:
        parameters = {'PostalCode': p}
        response = requests.get('https://ww3.yorkmaps.ca/arcgis/rest/services/YorkLocators/YorkPostal_Code/GeocodeServer/findAddressCandidates?f=pjson', params=parameters)
        attributes = response.json()['candidates']
        #wkid = response.json()['spatialReference']['wkid']
        coordinates = []
        for z in attributes:
            coord = z['location']
            coordinates.append(coord)

            for x in coordinates:
                long = x['x']
                lat = x['y']
                latitude.append(lat)
                longitude.append(long)


    df = pd.DataFrame({'Postal_Code': Postal, 'latitude': latitude, 'longitude': longitude})
    df.to_excel('Postal_Codes.xlsx')
    print('success')

if __name__ == '__main__':
    main()

