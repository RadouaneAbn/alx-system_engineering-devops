#!/usr/bin/python3
"""
This script return information about a users TODO list progress
"""
import json
from sys import argv
import requests


def info_per_id(user_id):
    """ This function return the some information about a user
    """
    total_tasks = done_tasks = 0
    task_titles = []
    url = "https://jsonplaceholder.typicode.com{}"
    user_info = requests.get(url.format("/users/" + user_id))
    all_tasks = requests.get(url.format("/todos"))

    user_info = user_info.json()
    all_tasks = all_tasks.json()

    name = user_info["name"]
    for task in all_tasks:
        if not str(task["userId"]) == user_id:
            continue

        total_tasks += 1
        if task["completed"]:
            done_tasks += 1
            task_titles.append(task["title"])

    return name, total_tasks, done_tasks, task_titles


if __name__ == "__main__":
    employee_id = argv[1]

    name, all_tasks, done_tasks, titles = info_per_id(employee_id)

    print("Employee {} is done with tasks({}/{}):".format(name, done_tasks,
                                                          all_tasks))
    for title in titles:
        print("\t {}".format(title))
