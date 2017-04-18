#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""football stats"""

from bs4 import BeautifulSoup
import requests
import json


response_obj = requests.get('http://www.cbssports.com/nfl/stats/playersort/nfl/year-2016-season-regular-category-touchdowns')

if response_obj.status_code == 200:
	
	html_source = response_obj.text
	
	soup_obj = BeautifulSoup(html_source, 'html.parser')
	
	data_table = soup_obj.find('table', {'class':'data'})
	
	title = soup_obj.find('tr', {'class': 'title'}).text
	print('title: ', title)

	# top 20 rows.
	top20_rows = data_table.findAll('tr')[3:23]
	top20stats = {}
	print(len(top20_rows))
	print(type(top20_rows))
	
	for i in range(len(top20_rows)):
		 
		 row_columns = top20_rows[i].findAll('td')
		 name = row_columns[0].text
		 pos = row_columns[1].text
		 team = row_columns[2].text
		 points = row_columns[4].text
		 touchdowns = row_columns[6].text
		 top20stats[i+1] = {}
		 top20stats[i+1]['name'] = name
		 top20stats[i+1]['pos'] = pos
		 top20stats[i+1]['team'] = team
		 top20stats[i+1]['points'] = points
		 top20stats[i+1]['touchdowns'] = touchdowns

	with open('footballtop20.json', 'w') as f:
		f.write(json.dumps(top20stats, indent = 4, separators=(',',':')))
		 


