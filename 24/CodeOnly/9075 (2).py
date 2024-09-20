with open('24_9075.txt') as file:
    data = file.readline()

for i in '13579':
    data = data.replace(i, '*')
for i in '02468':
    data = data.replace(i, '&')

data = data.replace('*&', '* &')
data = data.replace('&*', '& *')

data = data.split()

print(len(max(data, key=len)))
