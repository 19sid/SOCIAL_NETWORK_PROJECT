import sys
import xml.etree.ElementTree as etr

tree = etr.parse(sys.argv[1])
root= tree.getroot()
l=[]
u=[]

for name in root.iter('username'):
	l.append((name))

un=list(set(d.text for d in l))






	


