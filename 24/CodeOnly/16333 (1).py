with open('24_16333.txt') as file:
    data = file.readline()

count = 1
ans = 0

for i in range(len(data) - 1):
    let_1, let_2 = data[i], data[i + 1]
    if let_1 in 'QRW' and let_2 in 'QRW' or \
            let_1 in '124' and let_2 in '124':
        count = 1
    else:
        count += 1
    ans = max(ans, count)

print(ans)
