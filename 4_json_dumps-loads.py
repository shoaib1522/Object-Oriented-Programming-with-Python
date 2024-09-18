import json

# take user input to take the amount of data
number_of_data = int(input('Enter the number of data : '))
data = []

# take input of the data
for i in range(number_of_data):
    raw = input('Enter data '+str(i)+' : ')
    data.append(raw)

# dump information to that file
j = json.dumps(data)

print(j)

d = json.loads(j)

print(d)
