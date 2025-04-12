import json

action = input("Would you like to see your tasks? ")

if action == "y":
    # Reading JSON from a file
    with open('task.json', 'r') as file:
        loaded_task = json.load(file)

# Displaying the loaded data
print("Loaded JSON data:")
print(loaded_task)
