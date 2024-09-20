with open('24_14643.txt') as file:
    data = file.readline()

count = 3
ans = 0

for i in range(len(data) - 3):
    letters = data[i:i + 4]
    if letters == 'AXMM':
        count = 3
    else:
        count += 1
    ans = max(ans, count)

print(ans)
