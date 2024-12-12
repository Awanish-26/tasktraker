import json
import datetime as dt


# function that writes the updated date after each executiun
def writeFile():
    with open("data.json", mode="w+") as f:
        f.truncate()
        json.dump(data, f, indent=4)


# function to caluculate current date and time calcultion
def currentTime():
    now = dt.datetime.now()
    time = now.strftime("%H:%M:%S %Y-%m-%d ")
    return time


# Json Handling trie to open file if not found creates a new one with initial stucture
try:
    with open("data.json", mode="r+") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {"task": [], "id": [0]}

        if "task" not in data or not isinstance(data["task"], list):
            data = {"task": [], "id": [0]}
            json.dump(data, f, indent=4)
except FileNotFoundError:
    with open("data.json", mode="w") as f:
        data = {"task": [], "id": [0]}
        json.dump(data, f, indent=4)


# function to add a new task
def addtask(user_input):
    # create the template to add
    id = data["id"][-1] + 1
    datatoAdd = {
        "id": id,
        "description": user_input,
        "status": "todo",
        "createdAt": currentTime(),
        "updatedAt": currentTime()
    }

    data["task"].append(datatoAdd)
    data["id"].append(id)
    writeFile()
    print(f"Id of your task is {id}")


# update the task
def Update_task(get_id, get_update):
    for item in data["task"]:
        if item["id"] == get_id:
            item["description"] = get_update
            item["updatedAt"] = currentTime()
            break
    writeFile()


# function to delete a task
def delete_task(get_id):
    if get_id not in data["id"]:
        return "Invalid Id"

    for item in data["task"]:
        if item["id"] == get_id:
            data["task"].remove(item)
            data["id"].remove(get_id)
            break
    writeFile()


# function to set task status
def set_task_status(get_id, get_status):
    for item in data["task"]:
        if item["id"] == get_id:
            item["status"] = get_status
            item["updatedAt"] = currentTime()
    writeFile()


# lists all tasks
def all_task():
    for item in data["task"]:
        print(item)


# Listing tasks by status todo_task() done_task() progress_task()
def todo_task():
    for item in data["task"]:
        if item["status"] == "todo":
            print(item)


def done_task():
    for item in data["task"]:
        if item["status"] == "done":
            print(item)


def progress_task():
    for item in data["task"]:
        if item["status"] == "in_progress":
            print(item)


# main function
if __name__ == '__main__':
    while True:
        print()
        user_input = input("Task cli  ").split(maxsplit=2)
        operation = user_input.pop(0).lower()

        if operation == "add":
            description = " ".join(user_input)
            addtask(description)
        elif operation == "update":
            id = user_input.pop(0)
            description = " ".join(user_input)
            Update_task(int(id), description)
        elif operation == "delete":
            id = user_input.pop(0)
            delete_task(int(id))
        elif operation in ["mark-in-progress", "mark-done", "mark-todo"]:
            if operation == "mark-in-progress":
                operation = "in_progress"
            elif operation == "mark-done":
                operation = "done"
            else:
                operation = "todo"
            id = user_input.pop(0)
            set_task_status(int(id), operation)
        elif operation == "list" and len(user_input) == 0:
            all_task()
        elif operation == "list":
            status = user_input.pop(0)
            if status == "todo":
                todo_task()
            elif status == "done":
                done_task()
            elif status == "in_progress":
                progress_task()
        elif operation == "exit":
            print("Exiting the Program")
            break
        else:
            print("Invalid Input!")
