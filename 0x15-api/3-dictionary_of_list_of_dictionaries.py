#!/usr/bin/python3
"""
This script makes a json file containing all task owned by a user
"""
import json
import requests
from sys import argv


def all_users(url):
    """ This function return a list of all users
    """
    return requests.get(url.format("/users")).json()


def all_tasks(url):
    """ This function return a list of all tasks
    """
    return requests.get(url.format("/todos")).json()


def info_per_id(users_list, tasks_list):
    """ This function returns a dictionary that will be written in a json file
    """
    users = {}
    result = {}
    for user in users_list:
        tmp_id = str(user["id"])
        users[tmp_id] = user["username"]
        result[tmp_id] = []

    for task in tasks_list:
        tmp_id = str(task["userId"])
        result[tmp_id].append({
                "username": users[tmp_id],
                "task": task["title"],
                "completed": task["completed"]
            })

    return result


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com{}"
    users_list = all_users(url)
    tasks_list = all_tasks(url)

    final_result = info_per_id(users_list, tasks_list)

    with open("todo_all_employees.json", "w")as f:
        info = json.dumps(final_result)
        f.write(info)
