#!/usr/bin/python

import sys

try:
    sys.argv[1]
except:
    print 'usage: ./csvTranspose.py <filename>'
    sys.exit()

print 'invert: ', sys.argv[1]
filename = sys.argv[1]

infile = open(filename, 'r')
outfile = open (filename[:len(filename)-3] + 'mod.csv', 'w')

line = infile.readline();
rows = []
while(line != '\n' and line != ''):
    # takes all rows and splits them by the ',' character, appends the list to
     # the row variable
    rows.append(line.split(','))
#    print rows
    line = infile.readline()

for i in range(len(rows[0])):
    # writes the first entry of each of the rows to a new column
    for j in range(len(rows)):
        outfile.write(rows[j][i] + ',')
    outfile.write('\n')


infile.close()
outfile.close()
