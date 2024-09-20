with open('24_9075.txt') as file:
    data = file.readline()

ch = '02468'
nch = '13579'
count = 1
ans = 0

for i in range(len(data) - 1):
    let_1, let_2 = data[i], data[i + 1]
    if let_1 in ch and let_2 in nch or \
            let_1 in nch and let_2 in ch:
        count = 1
    else:
        count += 1
    ans = max(ans, count)

print(ans)
