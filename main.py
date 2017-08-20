import xml.etree.cElementTree as ET
import json

tree = ET.ElementTree(file='./data/xml/sample.xml')
root = tree.getroot()

kanjiList = []

for c in root.iter('character'):
    current = {}
    current['literal'] = c.find('literal').text
    kanjiList.append(current);

#print(json.dumps(kanjiList))
with open('./data/json/output.json', 'w') as outfile:
    json.dump(kanjiList, outfile)
