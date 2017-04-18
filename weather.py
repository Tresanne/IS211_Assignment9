#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""weather"""

import requests
from bs4 import BeautifulSoup
import json

month = '1'
year = '2015'
data = {}

res = requests.get('https://www.wunderground.com/history/airport/KNYC/2015/1/11/MonthlyHistory.html')
soup_obj = BeautifulSoup(res.text, 'html.parser')


obstable = soup_obj.find('table', {'id':'obsTable'})
all_tbodys = obstable.findAll('tbody')
print( 'No of days: ', len(all_tbodys[2:])	)
for i in range(1,len(all_tbodys)):
	all_tds = all_tbodys[i].findAll('td')
	data[i] = {}
	data[i]['high_Actual_temp'] = all_tds[1].text.replace('\n', '')
	data[i]['avg_Actual_temp'] = all_tds[2].text.replace('\n', '')
	data[i]['low_Actual_temp'] = all_tds[3].text.replace('\n', '')
with open('weather_data_'+month+'_'+year+'.json', 'w') as f:
		f.write(json.dumps(data, indent=4, separators=(':', ',')))
