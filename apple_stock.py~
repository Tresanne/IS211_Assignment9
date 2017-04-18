#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""stocks"""

import requests
import csv
import json



res = requests.get('http://chart.finance.yahoo.com/table.csv?s=AAPL')


if res.status_code == 200:
	decoded_content = res.content.decode('utf-8')
	cr = csv.reader(decoded_content.splitlines(), delimiter=',')
	mylist = list(cr)
	data = {}
	
	for row in mylist[1:]:
		
		data[row[0]] = row[4]

	with open('apple_stock.json', 'w') as f:
		f.write(json.dumps(data, indent=4, separators=(',',':')))

