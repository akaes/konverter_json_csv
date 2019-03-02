#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import json
import csv

# read json-file
with open('/Downloads/deputies.json') as json_file:
    json_data = json.load(json_file)
    
# open csv-file for writing
csv_data = open('/deputies.csv', 'w')

# create the csv writer object
csvwriter = csv.writer(csv_data)

count = 0

for json in json_data:
    if count == 0:
        header = json.keys()
        csvwriter.writerow(header)
        count += 1
    csvwriter.writerow(json.values())

csv_data.close()




