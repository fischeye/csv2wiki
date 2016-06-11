#!/usr/bin/env python
# -*- coding: utf-8 -*-

FilePath = 'data.csv'
Separator = ';'

# Read CSV-File
with open(FilePath, 'r') as oFile:
    content = oFile.read()
# Split File into Lines
contlist = content.split('\n')
wikitable = []

# Get Header
Header = contlist[0].split(Separator)
Columns = len(Header)

# Split Content to Lists
newlist = []
newlist.append(Header)
for idx in range(len(contlist)-1):
    splitline = contlist[idx+1].split(Separator)
    isTopic = True
    for idx2 in range(1,Columns):
        if (splitline[idx2] != ''):
            isTopic = False
            break
    if isTopic:
        wikitable.append(newlist)
        newlist = []
        newlist.append(Header)
    newlist.append(splitline)
wikitable.append(newlist)

# Calculate max Width
ColWidth = range(Columns)
for idx in range(Columns):
    ColWidth[idx] = 0
for table in wikitable:
    for row in table:
        for idx in range(Columns):
            if (len(row[idx]) > ColWidth[idx]):
                ColWidth[idx] = len(row[idx]) + 1

# Create Wiki Tables with Separators and add Spaces
wtable = []
for table in wikitable:
    firstrow = True
    for row in table:
        wtsep = '|'
        if firstrow:
            wtsep = '^'
        line = []
        # Check if its a Topic
        frow = True
        isTopic = True
        for checkcol in row:
            if frow:
                frow = False
            else:
                if not checkcol != '':
                    isTopic = False
        # Loop through Columns
        #if not isTopic:
        for idx in range(Columns):
            item = row[idx]
            # Add Spaces for calculated Width
            for idx2 in range(len(item), ColWidth[idx]):
                item = item + ' '
            line.append(item)
        # Join List to String with Separator
        linestr = wtsep + wtsep.join(line) + wtsep
        wtable.append(linestr)
        firstrow = False

# Search for UMLAUTE in Wikitable to add Space Characters
for line in wtable:
    found = False
    # Search for UMLAUTE
    for umlaut in ['ä', 'ö', 'ü']:
        if line.lower().find(umlaut) > -1:
            found = True
            wtsep = line[0]
            umlauts = {'ä': 0, 'ö': 0, 'ü': 0}
            break
    if found:
        # Count UMLAUTE in current Line
        for umlaut in umlauts:
            umlauts[umlaut] = line.lower().count(umlaut)
        # Locate UMLAUTE and add a Space bevor Separator
        for umlaut in umlauts:
            ucount = umlauts[umlaut]
            pos = 0
            for num in range(ucount):
                pos = line.lower().find(umlaut, pos+1)
                nextsep = line.find(wtsep, pos)
                line = line[:nextsep] + ' ' + line[nextsep:]
    print line
