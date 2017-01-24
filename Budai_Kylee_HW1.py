#! usr/bin/python3

import sys
import csv
import time

assert(len(sys.argv)==2)
attr = int(sys.argv[1])
assert(attr>=1 and attr<=10)

start = time.time()
inputfile = open('magic04.data')
data = csv.reader(inputfile,)
    #data = [(float(row[0:10])) for row in reader]
attrlist = []
for row in data:
    attrlist.append(float(row[attr-1]))

inputfile.close()
end = time.time()

print end-start
