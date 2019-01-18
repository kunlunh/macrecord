# -*- coding:utf-8 -*-
import json


def getrecordfromfile() :
	datalist = []

	with open('users.other') as f1:
		list1 = f1.readlines()
	for i in range(0, len(list1)):
		pos1 = list1[i].find('loc:')
		pos2 = list1[i].find('comment:')
		pos3 = list1[i].find('\r')
		datadict = {}
		datadict['ID'] = i
		datadict['MAC'] = list1[i][0:12]
		datadict['POS'] = list1[i][pos1+4:pos2].strip(' ')
		datadict['COMMENT'] = list1[i][pos2+8:pos3].strip(' ')
		datalist.append(datadict)
	print(datalist)
	return(datalist)
	

	#str_json = json.dumps(datalist)
	#return(str_json)

def setrecordtofile(allrecord) :

	allrecord = allrecord.strip(' ')
	allrecord = allrecord.strip('[{')
	allrecord = allrecord.strip('}]')
	listtmp = allrecord.split('},{')
	dictlist = []
	#convert string to list
	print(listtmp)
	for i in range(0, len(listtmp)):

		locCOMMENTfind = listtmp[i].find('COMMENT')
		locCOMMENTstart = locCOMMENTfind+10
		locCOMMENTend = listtmp[i].find('"',locCOMMENTstart)
		
		locMACfind = listtmp[i].find('MAC')
		locMACstart = locMACfind+6
		locMACend = listtmp[i].find('"',locMACstart)
		
		locPOSfind = listtmp[i].find('POS')
		locPOSstart = locPOSfind+6
		locPOSend = listtmp[i].find('"',locPOSstart)
		
		dictlist.append(listtmp[i][locMACstart:locMACend] + '    Cleartext-Password := "' + listtmp[i][locMACstart:locMACend] + '"  #loc:' + listtmp[i][locPOSstart:locPOSend] + ' comment:' +  listtmp[i][locCOMMENTstart:locCOMMENTend])
	
	outputstr = '\r\n'.join(dictlist)
	print(outputstr)
	
	
	fp = open('users-new.other', 'w')
	
	fp.write(outputstr)
	fp.close()

	#return(datalist)
