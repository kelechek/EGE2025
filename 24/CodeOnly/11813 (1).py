with open('../Files/24_11813.txt') as file:
    data = file.readline()

gl = 'AEIOUY'
count = 1
ans = 0

for i in range(len(data) - 1):
    let_1, let_2 = data[i], data[i + 1]
    if let_1 in gl and let_2 in gl or \
            let_1 not in gl and let_2 not in gl:
        count = 1
    else:
        count += 1
    ans = max(ans, count)

print(ans)
