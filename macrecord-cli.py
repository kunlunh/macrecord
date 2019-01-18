# -*- coding:utf-8 -*-
import json



datalist = []

with open('users.other') as f1:
	list1 = f1.readlines()
for i in range(0, len(list1)):
	pos1 = list1[i].find('loc:')
	pos2 = list1[i].find('comment:')
	pos3 = list1[i].find('\r')
	datadict = {}
	datadict['ID'] = i
	datadict['MAC'] = list1[i][0:11]
	datadict['POS'] = list1[i][pos1+4:pos2].strip(' ')
	datadict['COMMENT'] = list1[i][pos2+8:pos3].strip(' ')
	#datalist[i][data['mac']] = list1[i][20:30]
	#str = list1[i][0:11]
	datalist.append(datadict)
print(list1)

str_json = json.dumps(datalist)
print(str_json)