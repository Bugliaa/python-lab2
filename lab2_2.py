import sys

file = open(sys.argv[1], 'r')

cmd = '0'

myList = []

for task in file:
    task = task.split('\n')[0]
    myList.append(task)

file.close()

print("1. Insert a new task")
print("2. Remove a task")
print("3. Show all existing tasks, sorted in alphabetical order")
print("4. Save the to-do list to the text file")
print("5. Close the program")

while cmd != '5':

    print("Enter a command: ")
    cmd = input()

    if cmd == '1':
        print("Enter the task to insert: ")
        task = input()
        task = task
        myList.append(task)

    if cmd == '2':
        print("Enter the task to delete: ")
        task = input()
        myList.remove(task)

    if cmd == '3':
        print("My to-do list:")
        print(sorted(myList))

    if cmd == '4':
        # print("Enter file name: ")
        # fn = input()
        # file1 = open(fn, 'w+')
        file = open(sys.argv[1], 'w+')
        for task in myList:
            file.write("%s \n" % task)
        file.close()
