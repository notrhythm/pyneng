# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

enter_ip = input('Enter IP-address: ')

try:
    entered_ip = [int(x) for x in enter_ip.split('.')]
except ValueError:
    print('Incorrect IPv4 address')
else:
    check_octet = [octet for octet in entered_ip if 0 <= octet <= 255]

if len(check_octet) != 4:
    print('Incorrect IPv4 address')
if 1 <= int(entered_ip[0]) <= 223:
    print('unicast')
elif 224 <= int(entered_ip[0]) <=239:
    print('multicast')
elif enter_ip == '255.255.255.255':
    print('local broadcast')
elif enter_ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')

