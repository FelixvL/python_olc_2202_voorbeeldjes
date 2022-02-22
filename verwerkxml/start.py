import xml.etree.ElementTree as ET
import pandas as pd

#xml_data = open('boeken.xml', 'r').read()  # Read file

deboekendf = pd.read_xml('boeken.xml')
print(deboekendf.head(5))








#root = ET.XML(xml_data)

#data = []
#cols = []

#for i, child in enumerate(root):
#    print(i)