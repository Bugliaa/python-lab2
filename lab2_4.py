import sys

file = open(sys.argv[1])
myList = []

for task in file:
    print(task)
    # if dn['urgent']:
    #     myList.append(task)

print("Urgent tasks:")

print(myList)

