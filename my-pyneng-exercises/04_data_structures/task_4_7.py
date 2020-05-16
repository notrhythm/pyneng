# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

'''
#first try
mac = 'AAAA:BBBB:CCCC'

mac2 = mac.replace(':', '')
mac3 = int(mac2, 16)
mac4 = bin(mac3)
mac5 = mac4[2:]
'''

#second try
mac = 'AAAA:BBBB:CCCC'

binmac = (bin(int(mac.replace(':', ''), 16)))[2:]
print(binmac)














