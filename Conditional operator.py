x = 997

print('Добро пожаловать в Казахстан!)')
if x > 0:
    print('С прибытием!')
print('Всего хорошего!')

y, z = 21, 43

if y < z:
    print('Действительно')
if y < z and z > 33:
    print('Доступ разрешён')
if y > 16 and (z > 39 or y == z):
    print('Доступ почти разрешён')
if y >= 20 and z != 43:
    print('Неверно')

if '56' > '230':
    print('Естественно')
if '27' < '2719':
    print('Конечно')
if [7, 4] < [8, 3]:
    print('А как же')

#  if '53' > 25:     - Ошибка, так как данная операция между типом str и int неподдерживается.
#     print('Да')
# if [5, 3] > 25:    - Ошибка, так как данная операция между типом list и int неподдерживается.
#     print('Ага')
if '53' != 25:
    print('Хмм...ДА')
