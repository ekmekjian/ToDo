#! usr/bin/python
#!/usr/bin/env python
#
# This is the To-Do list program creates a list full of tasks entered
# in the command line as syste arguments then manipulated based to user
# enter flags then (still not developed ->) displayed on a transparent
# widget on a desktop
#
# Notes:
#
# Functions need to be build or debugged: sortedDic
#
# Current error: none :)
#




import os, sys
from random import randint

# load all contents of a file to a dictionary
def loadDic(dic):
    dic = {}
    with open("list.txt") as f:
        for line in f:
            temp = line.split(':')
            key = temp[0]
            val = temp[1].rstrip()
            dic[key] = val
    return dic

# sorts from smallest to largest
def sortempDic(tempDic):
    sortThis = list(tempDic.keys())
    sortedDic = {}
    return sortedDic

# adds new entry to file
def addNew(text,tempDic):
    id = randint(1000,9999)
    newString = ' '.join([str(x) for x in text])
    # TODO: check if id exists

    tempDic[id] = newString
    #tempDic = sortempDic(tempDic)
    return tempDic

# Deletes by Id
def delete(idK,passedDic):
    tempDic = {}
    for key in passedDic:
        if key == idK:
            continue
        else:
            tempDic[key] = passedDic[key]
    return tempDic

# Appends to file the contents of the dictionary
def writeFile(tempDic):
    writer = open("list.txt","w+")

    for key in tempDic:
        line = str(key)+":"+str(tempDic[key])+"\n"
        writer.write(line)
    writer.close()



dictMain = {}
# load file to the dictionary to work with
dictMain = loadDic(dictMain)

if sys.argv[1]=='rm':
    dictMain=delete(sys.argv[2],dictMain)
    writeFile(dictMain)
else:
    dictMain = addNew(sys.argv[1:],dictMain)
    writeFile(dictMain)
