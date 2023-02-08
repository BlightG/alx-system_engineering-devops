#!/usr/bin/python3
"""
script that returns employee ID and TO/DO list progress
"""

from sys import argv
import json
import urllib.request


def parse_response(response):
    """converts response from byte to list type """
    str_response = response.decode('utf-8')
    list_response = json.loads(str_response)
    return (list_response)


if __name__ == '__main__':
    if len(argv) <= 1:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit()

    jsondict = {}

    with urllib.request.urlopen('https://jsonplaceholder.typicode.com' +
                                f'/users/{argv[1]}') as req:
        list_response = parse_response(req.read())
        user = list_response.get("name")

    with urllib.request.urlopen('https://jsonplaceholder.typicode.com' +
                                f'/todos?userId={argv[1]}') as req:
        list_response = parse_response(req.read())
        new_list = []
        for dct in list_response:
            new_dict = {}
            new_dict = {"task": dct.get('title'), 
                        "completed": dct.get('completed'),
                        "username": user}
            new_list.append(new_dict)
        jsondict[f'{argv[1]}'] = new_list

    with open(f'{argv[1]}.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(jsondict))
