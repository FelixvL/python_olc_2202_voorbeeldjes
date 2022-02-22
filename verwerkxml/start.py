import xml.etree.ElementTree as ET
import pandas as pd

#xml_data = open('boeken.xml', 'r').read()  # Read file

deboekendf = pd.read_xml('boeken.xml')
#print(deboekendf.head(5))
print(deboekendf.columns)
print(deboekendf['title'])

for obj, boek in deboekendf.iterrows():
    if boek['price'] < 10 :
        print(boek['title'])








#root = ET.XML(xml_data)

#data = []
#cols = []

#for i, child in enumerate(root):
#    print(i)