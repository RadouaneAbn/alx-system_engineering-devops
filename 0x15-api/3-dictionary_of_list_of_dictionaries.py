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
    """ This fucntion return a list of all tasks
    """
    return requests.get(url.format("/todos")).json()


def info_per_id(users_list, tasks_list):
    """ This function returns a dictionary that will be written in a json file
    """
    result_dict = {}
    result_list = []
    for user in users_list:
        username = user["username"]
        user_id = user["id"]
        tmp_list = []
        for task in tasks_list:
            if task["userId"] != user_id:
                continue
            tmp_list.append({
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
                })
            tasks_list.remove(task)

        result_dict[str(user_id)] = list(tmp_list)

    return result_dict


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com{}"
    users_list = all_users(url)
    tasks_list = all_tasks(url)

    final_result = info_per_id(users_list, tasks_list)

    with open("todo_all_employees.json", "w")as f:
        info = json.dumps(final_result)
        f.write(info)
