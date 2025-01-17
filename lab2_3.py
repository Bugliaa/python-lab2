import sys

file = open(sys.argv[1])

print("1. Insert a new task")
print("2. Remove a task")
print("3. Remove a task containing a specified substring")
print("4. Show all existing tasks, sorted in alphabetical order")
print("5. Close the program")

cmd = '0'

myList = []

for task in file:
    myList.append(task)

while cmd != '5':

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
        print("Enter the substring: ")
        sub = input()

        for task in myList:
            if sub in task:
                myList.remove(task)

    if cmd == '4':
        print("My to-do list:")
        print(sorted(myList))

