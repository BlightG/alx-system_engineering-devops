#!/usr/bin/python3
"""
script that write to a csv file
employee ID and TO/DO list progress
"""

import csv
from sys import argv
import json
import urllib.request


def parse_response(response):
    """converts response from byte to list type""" 
    str_response = response.decode('utf-8')
    list_response = json.loads(str_response)
    return (list_response)


if __name__ == "__main__":
    if len(argv) <= 1:
        print("Usage: ./1-export_to_csv.py <employee_id>")
        exit()


    with urllib.request.urlopen('https://jsonplaceholder.typicode.com' +
                                f'/users/{argv[1]}') as req:
        list_response = parse_response(req.read())
        user = list_response.get("name")
    
    with urllib.request.urlopen('https://jsonplaceholder.typicode.com' +
                                f'/todos?userId={argv[1]}') as req:
        list_response = parse_response(req.read())

    with open(f'{argv[1]}.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f,quoting=csv.QUOTE_ALL)

        for dct in list_response:
            response_value = []
            response_value.append(dct.get('userId'))
            response_value.append(user)
            response_value.append(dct.get('completed'))
            response_value.append(dct.get('title'))
            writer.writerow(response_value)
