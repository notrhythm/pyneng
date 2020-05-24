# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

while True:

    enter_ip = input('Enter IP-address: ')

    try:
        entered_ip = [int(x) for x in enter_ip.split('.')]
    except ValueError:
        print('Incorrect IPv4 address')
        continue
    else:
        check_octet = [octet for octet in entered_ip if 0 <= octet <= 255]


    if len(check_octet) != 4:
        print('Incorrect IPv4 address')
        continue
    if 1 <= int(entered_ip[0]) <= 223:
        print('unicast')
        break
    elif 224 <= int(entered_ip[0]) <=239:
        print('multicast')
        break
    elif enter_ip == '255.255.255.255':
        print('local broadcast')
        break
    elif enter_ip == '0.0.0.0':
        print('unassigned')
        break
    else:
        print('unused')
        break
    print('Please, enter IP-address again')