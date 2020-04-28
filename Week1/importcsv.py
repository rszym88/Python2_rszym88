# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import csv

print('***********************************************************************')
print("Hello Neo...")
print()
print("Follow the white rabbit.....")
print('***********************************************************************')

file = 'studentInfoCSV.csv'
studentInfo = {}
tmpSave = []
def printHeaders():
    with open(file) as csvFile:
        dReader = csv.DictReader(csvFile)
        headers = dReader.fieldnames
        tmpUsr = ''
        #print(headers)
        count = 0
        for row in dReader:
            tmpEntry1 = {}
            #tmpStr = x + ':' + row[x]
            tmpUsr = row['userNamer']
            #if tmpUsr not in studentInfo:
            #print(row)
            for x in row:
                tmpEntry0 = []
                if x != "userNamer":
                    #print(x)
                    tmpEntry1.update({x: row[x]})
            studentInfo.update({tmpUsr: tmpEntry1})
            print(tmpUsr)
            print(tmpEntry1)
            for y in studentInfo:
                tmp = studentInfo[y]
                current = 0
                while current < len(tmp):
                    saveit = []
                    saveit.append(tmp[current])
                    print('........................')
                    print(y, ':')
                    print('........................')
                    tmpD = saveit[current]
                    #print('**' , tmpD)
                    for a in tmpD:
                        xx = 0
                        newList = []
                        if a == 'iconDataList':
                            print('****', tmpD[a])
                            tmpStr = tmpD[a]
                            tmpStr2 = ''
                            print('****', tmpStr)
                            for c in tmpStr:
                               print(c)
                               if c.isnumeric():
                                   tmpStr2 = tmpStr2 + c
                                   while len(newList) < 10:
                                       cc = tmpStr2[xx:xx+10]
                                       newList.append(cc)
                                       print(cc)
                                       cc = ''
                                       xx = xx + 10
                            print(newList)
                        
                        
                        
                        #print(len(tmpStr))
                        '''
                        while xx <= len(tmpStr):
                            if tmpStr[xx].isnumeric():
                                tmpStr2 = tmpStr2 + tmpStr[xx]
                                #c2 = 0
                                while len(tmpStr2) != 10:
                                    newList.append(tmpStr2)
'''
                                 

                        #print('    ' + a + ': ' + tmpD[a])
                #for a in :
                 #   print(a, saveit[a])
                current += 1
            #for z in int(len(tmp)):
                #print()
                print('........................')    
                #print(studentInfo['rszym88'])
                #qq = studentInfo['rszym88']
printHeaders()                
