#!/usr/bin/python3
"""
Script to gather data from an api
"""

import requests
from sys import argv


if __name__ == "__main__":
    emp_id = argv[1]
    user_info = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(emp_id))
    todo_info = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id))

    emp_data = user_info.json()
    todo_data = todo_info.json()

    total_tasks = len(todo_data)
    done_tasks = sum(task.get('completed') for task in todo_data)
    emp_name = emp_data.get("name")

    print("Employee {} is done with tasks ({}/{}):".format(
        emp_name, done_tasks, total_tasks))

    for task in todo_data:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
