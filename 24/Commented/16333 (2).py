# Открываем файл и считываем строку
with open('../Files/24_16333.txt') as file:
    data = file.readline()

# Заменяем все цифры '2' и '4' на '1', чтобы упростить обработку
data = data.replace('2', '1').replace('4', '1')

# Заменяем все буквы 'W' и 'R' на 'Q' для упрощения логики (работаем с одной буквой вместо нескольких)
data = data.replace('W', 'Q').replace('R', 'Q')

# Пока в строке встречаются последовательности двух одинаковых символов 'QQ' (буквы)
# или '11' (цифры), заменяем их на такие же символы с пробелом между ними для разделения
while 'QQ' in data or '11' in data:
    data = data.replace('QQ', 'Q Q').replace('11', '1 1')

# Разбиваем строку по пробелам на отдельные группы символов
data = data.split()

# Находим самую длинную группу и выводим её длину
print(len(max(data, key=len)))
