__author__ = 'warior'
__mastermind__ = 'http://habrahabr.ru/post/88972/'

#Длинные строки кода и их продолжения
def ras(first, second, third,
        fourth, fifth, sixth):
    output = (first + second + third
              + fourth + fifth + sixth)
    return output

VeryLong = 'Очень длинная строка' + \
    'которая продолжается'

#неявное объеденение
print('o''n''e')
text = ('Первая и'' вторая')
print(text)

#Составные операторы
foo = 'Qwe?'
if foo == 'prum':
    print('Uh!')
qwe = ras(1, 2, 3, 4, 5, 6)
print(qwe)

#Хитрые кортежи
a = 2
b = 5
a, b = b, a
l = ['David', 'Pythonista', '+1-514-555-1234']
name, title, phone = l

#Ещё строки
colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)
print('Choose', ', '.join(colors[:-1]),'or', colors[-1])