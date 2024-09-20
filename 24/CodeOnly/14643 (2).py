with open('24_14643.txt') as file:
    data = file.readline()

data = data.replace('AXMM', 'AXM XMM')

data = data.split()

print(len(max(data, key=len)))
