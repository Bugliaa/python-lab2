task1 = {'todo': 'call John for AmI project organization', 'urgent': True}
task2 = {'todo': 'buy a new mouse', 'urgent': True}
task3 = {'todo': 'find a present for Angelina’s birthday', 'urgent': False}
task4 = {'todo': 'organize mega party (last week of April)', 'urgent': False}
task5 = {'todo': 'book summer holidays', 'urgent': False}
task6 = {'todo': 'whatsapp Mary for a coffee', 'urgent': False}

myList = []
urList = []

myList.append(task1)
myList.append(task2)
myList.append(task3)
myList.append(task4)
myList.append(task5)
myList.append(task6)

for task in myList:
    if task['urgent']:
        urList.append(task['todo'])

print("Urgent tasks:")

print(urList)