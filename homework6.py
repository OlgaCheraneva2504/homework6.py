my_dict = {'Литл гром': 15245963, 'Пушистые мошенники': 9845324, 'Лонки': 25165398}
print(my_dict)
print(my_dict['Литл гром'], ',', my_dict.get('Зверолэнд'))
my_dict.update({'Тайна магазина игрушек': 3654851,
               'Веселая ферма': 1263541})
a = my_dict.pop('Пушистые мошенники')
print(a)
print(my_dict)



my_set = {1508, 2202, 1712, 2651, 2202, 1762, 1508, 3684, 2651, 2202}
print(my_set)
my_set.update({1732, 2896})
my_set.discard(1508)
print(my_set)