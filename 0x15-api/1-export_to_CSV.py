#!/usr/bin/python3
"""script that write to a csv file employee ID and TO/DO list progress """
import csv
from sys import argv
import json
import urllib.request

if __name__ == '__main__':
    if len(argv) <= 1:
        print("Usage: ./1-export_to_csv.py <employee_id>")
        exit()

    def parse_response(response):
        """converts response from byte to list type """ 
        str_response = response.decode('utf-8')
        list_response = json.loads(str_response)
        return (list_response)

    with urllib.request.urlopen('https://jsonplaceholder.typicode.com' +
                                f'/todos?userId={argv[1]}') as req:
        list_response = parse_response(req.read())

    with open(f'{argv[1]}.csv', 'w', encoding='UTF8', newline='') as f:

        writer = csv.writer(f)
        for dct in list_response:
            response_value = []
            for key, values in dct.items():
                if key != 'id':
                    response_value.append(values)
            # print(response_value)
            writer.writerow(response_value)
