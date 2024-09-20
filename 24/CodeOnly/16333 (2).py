with open('24_16333.txt') as file:
    data = file.readline()

data = data.replace('2', '1').replace('4', '1')
data = data.replace('W', 'Q').replace('R', 'Q')

while 'QQ' in data or '11' in data:
    data = data.replace('QQ', 'Q Q').replace('11', '1 1')

data = data.split()

print(len(max(data, key=len)))
