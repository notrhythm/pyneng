# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


'''first try

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

list1 = (ospf_route.split())

print(list1)
print(("%-20s %-15s") % ('Protocol:', list1[0]+'SPF'))
print(("%-20s %-15s") % ('Prefix:', list1[1]))
print(("%-20s %-15s") % ('AD/Metric:', list1[2].strip('[]')))
print(("%-20s %-15s") % ('Next-Hop:', list1[4].strip(',')))
print(("%-20s %-15s") % ('Last Update:', list1[5].strip(',')))
print(("%-20s %-15s") % ('Outbound Interface:', list1[6]))

'''

#second try

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

list1 = (ospf_route.split())

template = '''
Protocol:                     {0:<30}
Prefix:                       {1:<30}
AD/Metric:                    {2:<30}
Next-Hop:                     {3:<30}
Last Update:                  {4:<30}
Outbound Intrface:            {5:<30}
'''

print(template.format(list1[0]+'SPF', list1[1], list1[2].strip('[]'), list1[4].strip(','), list1[5].strip(','), list1[6]))