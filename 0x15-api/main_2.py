#!/usr/bin/python3
"""
Check student .CSV output of user information
"""

import csv
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info(id):
    """ Check CSV formatting """

    response = requests.get(todos_url).json()
    with open(str(id) + ".csv", 'r') as f:
        output = f.read().strip()
        count = 0
        flag = 0
        for i in response:
            if i['userId'] == id:
                url = users_url + str(i['userId'])
                usr_resp = requests.get(url).json()
                line = '"' + str(i['userId']) + '","' + usr_resp[0]['username'] + '","' + str(i['completed']) + '","' + i['title'] + '"'
                count += 1
                if not line in output:
                    print("Task {} Formatting: Incorrect".format(count))
                    flag = 1

    if flag == 0:
        print("Formatting: OK")


if __name__ == "__main__":
    user_info(int(sys.argv[1]))
