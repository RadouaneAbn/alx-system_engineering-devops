#!/usr/bin/python3
"""
This script makes a json file containing all task owned by a user
"""
import json
import requests
from sys import argv


def info_per_id(user_id):
    """ This function returns a dictionary that will be written in a json file
    """
    tasks_list = []
    url = "https://jsonplaceholder.typicode.com{}"
    user_info = requests.get(url.format("/users/" + user_id)).json()
    all_tasks = requests.get(url.format("/todos")).json()

    username = user_info["username"]
    for task in all_tasks:
        if not str(task["userId"]) == user_id:
            continue

        current_task_info = {
                "task": task["title"],
                "completed": task["completed"],
                "username": username
                }
        tasks_list.append(current_task_info)

    tasks_dict = {user_id: tasks_list}

    return tasks_dict


if __name__ == "__main__":
    employee_id = argv[1]

    all_tasks = info_per_id(employee_id)

    with open("{}.json".format(employee_id), "w")as f:
        info = json.dumps(all_tasks)
        f.write(info)
