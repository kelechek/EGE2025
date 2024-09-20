with open('24_9850.txt') as file:
    data = file.readline()

for i in 'LISENOK':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))
