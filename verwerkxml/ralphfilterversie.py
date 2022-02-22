import xml.etree.ElementTree as ET
import pandas as pd

#xml_data = open('boeken.xml', 'r').read()  # Read file
df = pd.read_xml("boeken.xml")

dfCheap = df[df.price < 20]
dfCheap = dfCheap.filter(items=["title"])
dfCheap.to_csv("test.csv",";")