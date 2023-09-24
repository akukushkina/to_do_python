import json

try:
    with open("tasks.json", "r") as file:
        list = json.load(file)
except FileNotFoundError:
    list = []

    # ask user wht they want to do
    user_want = input(
        "What do you want to do today: see the list (1), add task (2), mark as done (3), delete task (4): "
    )

    # communivate with user
    if user_want == "1":
        print(list)
    elif user_want == "2":
        # create a new todo dictionary for each task.
        todo = {
            "title": input("Add title: "),
            "description": input("Add descritption: "),
            "completed": False,
        }
        list.append(todo)
    elif user_want == "3":
        done = input("Enter a title: ")
        for item in range(0, len(list) - 1):
            if list[item]["title"].lower() == done.lower():
                list[item]["completed"] = True
    elif user_want == "4":
        delete = input("Enter title of the task you want to delete: ")
        for item in range(0, len(list) - 1):
            if list[item]["title"].lower() == delete.lower():
                del list[item]

    with open("tasks.json", "w") as file:
        json.dump(list, file)
