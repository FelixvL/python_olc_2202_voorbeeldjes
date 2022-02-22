import xml.etree.ElementTree as ET
import pandas as pd

#xml_data = open('boeken.xml', 'r').read()  # Read file

deboekendf = pd.read_xml('boeken.xml')
#print(deboekendf.head(5))
print(deboekendf.info())
print(deboekendf['title'])
data = []
deboeken = pd.DataFrame(data)


for obj, boek in deboekendf.iterrows():  ## dit stukje werkt nog niet
    if boek['price'] < 10 :
        print(boek['title'])
        #global deboeken
        deboeken.add(boek['title'])

print("===========================")
print(deboeken)

deboekendf.to_csv('ffkijken.csv',';')








#root = ET.XML(xml_data)

#data = []
#cols = []

#for i, child in enumerate(root):
#    print(i)