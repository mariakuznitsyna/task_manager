import json

action = input("Hi! How can I help you today? \n 1. Add new task \n 2. Check my current tasks ")

class Task:
    def __init__(self, name, status):
        self.name = name
        self.status = status

#Define a custom encoding function
def encode_task(obj):
    if isinstance(obj, Task):
        return {'Task Name': obj.name, 'Task Status': obj.status}
    return obj

if action == "1":
    task_name = input("Task name: ")
    task_status = input("Task status: ")

    # Create an instance of the custom class
    task_object = Task(f"{task_name}", f"{task_status}")

    # Writing JSON to a file with custom encoding
    with open('task.json', 'w') as file:
        json.dump(task_object, file, default=encode_task, indent=4)

    print("New task has been added to your To-Do!")
else:
    with open('task.json', 'r') as file:
        loaded_task = json.load(file)
    # Displaying the loaded data
    print("Current tasks:")
    print(loaded_task)
