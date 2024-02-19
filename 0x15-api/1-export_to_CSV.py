#!/usr/bin/python3
"""
Script using REST API
Exports data in CSV format
"""

import requests
import sys


if __name__ == "__main__":

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    response = requests.get(url)
    employee_name = response.json().get("name")

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    done = 0
    done_tasks = []

    with open("{}.csv".format(employee_id), "w") as csv_file:
        for task in tasks:
            csv_file.write('"{}","{}","{}","{}"\n'.format(
                employee_id, employee_name, task.get("completed"),
                task.get("title")))
