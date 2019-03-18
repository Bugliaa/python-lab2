print("1. Insert a new task")
print("2. Remove a task")
print("3. Show all existing tasks, sorted in alphabetical order")
print("4. Close the program")

cmd = '0'

myList = []

while cmd != '4':

    print("Enter a command: ")
    cmd = input()

    if cmd == '1':
        print("Enter the task to insert: ")
        task = input()
        myList.append(task)

    if cmd == '2':
        print("Enter the task to delete: ")
        task = input()
        myList.remove(task)

    if cmd == '3':
        print("My to-do list:")
        print(sorted(myList))

