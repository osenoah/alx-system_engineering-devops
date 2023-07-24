#!/usr/bin/python3

import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetching the employee's information
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data["name"]

    # Fetching the employee's TODO list
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Counting completed tasks and total tasks
    completed_tasks = [task for task in todos_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    # Printing the output in the required format
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: The employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

