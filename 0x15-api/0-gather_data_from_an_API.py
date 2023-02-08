#!/usr/bin/python3
"""script that returns employee ID and TO/DO list progress """

from sys import argv
import json
import urllib.request

if __name__ == '__main__':
    if len(argv) <= 1:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit()

    task_completed = 0
    title_list = []

    def parse_response(response):
        """converts response from byte to list type """ 
        str_response = response.decode('utf-8')
        list_response = json.loads(str_response)
        return (list_response)

    with urllib.request.urlopen('https://jsonplaceholder.typicode.com' +
                                f'/users/{argv[1]}') as req:
        list_response = parse_response(req.read())
        user = list_response.get("name")

    with urllib.request.urlopen('https://jsonplaceholder.typicode.com' +
                                f'/todos?userId={argv[1]}') as req:
        list_response = parse_response(req.read())
        for dct in list_response:
            if dct['completed'] is True:
                task_completed = task_completed + 1
                title_list.append(dct.get('title'))
        print(f'Employee {user} is done with tasks' +
              f' ({task_completed}/{len(list_response)}):')
        for title in title_list:
            print(f'\t {title}')
