# Automated-Geocoding

I wrote this program for my work at the non-profit Urban Farm Initiative. It is a simple program that uses webscraping to get postal codes for splash pads from a local government website then uses them as parameteres for an ArcGIS geocoder API service. The rest is extracting the coordinates from the JSON response and saving them.

You will notice that I have included how to get the "wkid" from the JSON response as well. I included it because it is necessary for making shapefiles in a python envitonment using PyQGIS or Arcpy. Here are some links that explain how to do that:

https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/vector.html#creating-vector-layers
https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/xy-table-to-point.htm

You would use wkid to refere to the proper spatial references here.
