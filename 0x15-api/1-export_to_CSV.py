#!/usr/bin/python3
"""
This script makes a csv file containing all task owned by a user
"""
import csv
import requests
from sys import argv


def info_per_id(user_id):
    """ This function returns a list that will be written in a csv file
    """
    total_tasks = done_tasks = 0
    tasks_status = []
    url = "https://jsonplaceholder.typicode.com{}"
    user_info = requests.get(url.format("/users/" + user_id)).json()
    all_tasks = requests.get(url.format("/todos")).json()

    for task in all_tasks:
        current_id = str(task["userId"])
        if not current_id == user_id:
            continue
        tasks_status.append([current_id,
                             user_info["username"],
                             str(task["completed"]),
                             task["title"]
                             ])
    return tasks_status


if __name__ == "__main__":
    employee_id = argv[1]

    all_tasks = info_per_id(employee_id)

    with open("{}.csv".format(employee_id), "w")as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(all_tasks)
