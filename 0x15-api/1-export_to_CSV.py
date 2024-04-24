#!/usr/bin/python3
"""
This script exports data from the JSONPlaceholder API to a CSV file.
It retrieves all tasks owned by a specified user and exports them to a CSV file.
"""

import requests
import sys
import csv


if __name__ == "__main__":
    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()

    csv_file = f"{emp_id}.csv"

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([todo["userId"], todo["title"], todo["completed"], todo["title"]])

    print(f"CSV file '{csv_file}' created successfully.")
