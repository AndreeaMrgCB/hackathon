import csv
import json
import os
 
csv_file_name = "Sample-Spreadsheet-100-rows.csv"
json_file_name ="emptyjson.json" # you will need to change this to your json file name

def csv_to_json(csv_file_name, json_file_name):

    data_dict = {}
    key = 0
    with open(csv_file_name, 'r') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
 
        for rows in csv_reader:

            key += 1
            data_dict[key] = rows
 
    print(data_dict)

    if os.path.exists(json_file_name) or os.path.getsize(json_file_name) == 0:
        with open(json_file_name, 'w', encoding='utf-8') as json_file_handler:
            json.dump(data_dict, json_file_handler, indent=4)
    else:
            print("hello world")
 
 
csv_to_json(csv_file_name, json_file_name)