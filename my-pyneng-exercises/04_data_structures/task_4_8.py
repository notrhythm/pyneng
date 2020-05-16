# -*- coding: utf-8 -*-
'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#first try

ip = '10.1.1.1'

# ipsplit = ip.split('.')
# ip1 = ipsplit[0]
# ip2 = ipsplit[1]
# ip3 = ipsplit[2]
# ip4 = ipsplit[3]

ip1, ip2, ip3, ip4 = ip.split('.')

ipint1 = int(ip1)
ipint2 = int(ip2)
ipint3 = int(ip3)
ipint4 = int(ip4)

template = '''
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

print(template.format(ipint1, ipint2, ipint3, ipint4))














