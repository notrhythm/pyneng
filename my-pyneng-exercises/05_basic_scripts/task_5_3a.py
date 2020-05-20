# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

mode = input('Enter switchport mode (access/trunk): ')
interface = input('Enter type and number of interface: ')

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

dictionary = {'access': access_template,
              'trunk': trunk_template,
              'mode_access': 'Enter vlan number: ',
              'mode_trunk': 'Enter allowed vlans: '}

vlan_mode = 'mode_' + mode
vlans = input(('{}').format(dictionary.get(vlan_mode)))

print('-' * 50 + '\n')
print('interface ' + interface)
print(('\n'.join(dictionary.get(mode))).format(vlans))
