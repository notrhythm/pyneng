# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

'''
#first try

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

command3 = command1[30::]
command4 = command2[30::]

command5 = command3 + ',' + command4

command6 = command5.split(',')

command7 = set(command6)

command8 = sorted(command7)

command8.remove('2')
command8.remove('5')
command8.remove('9')

'''

'''
#second try

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

comm1 = command1.split()
vlan1 = comm1[-1].split(',')
print(vlan1)

comm2 = command2.split()
vlan2 = comm2[-1].split(',')
print(vlan2)

vlans = (set(vlan1) & set(vlan2))
print(vlans)
vlans = sorted(vlans)
print(vlans)

'''
#third try

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

vlans = sorted((set(((command1.split())[-1].split(',')))) & (set(((command2.split())[-1].split(',')))))
print(vlans)






















