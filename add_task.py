import json

action = input("Would you like to add a new task? ")

if action == "y":
    #User input 
    task_name = input("Task name: ")
    task_status = input("Task status: ")
    #Create JSON
    task = {
    "name": f"{task_name}",
    "status": f"{task_status}"
} 
    
    # Writing JSON to a file
    with open('task.json', 'w') as file:
       json.dump(task, file)
else:
    print("Alright, have a nice day!")




print("JSON data has been stored in 'task.json'")