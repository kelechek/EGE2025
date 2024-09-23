# Открываем текстовый файл для чтения
with open('24_9075.txt') as file:
    data = file.readline()  # Считываем первую строку файла

# Заменяем нечетные цифры на символ '*'
for i in '13579':
    data = data.replace(i, '*')

# Заменяем четные цифры на символ '&'
for i in '02468':
    data = data.replace(i, '&')

# Заменяем последовательности '*&' и '&*' на '* &' и '& *', чтобы разделить четные и нечетные
data = data.replace('*&', '* &')
data = data.replace('&*', '& *')

# Разделяем строку по пробелам, чтобы получить список подстрок
data = data.split()

# Находим максимальную длину строки в списке и выводим ее
print(len(max(data, key=len)))
