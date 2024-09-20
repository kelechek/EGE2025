with open('24_11813.txt') as file:
    data = file.readline()

gl = 'eyuioa'.upper()
sg = 'qwrtpsdfghjklzxcvbnm'.upper()

for i in gl:
    data = data.replace(i, 'E')
for i in sg:
    data = data.replace(i, 'G')

while 'GG' in data or 'EE' in data:
    data = data.replace('GG', 'G G').replace('EE', 'E E')

data = data.split()
print(len(max(data, key=len)))
