# Работа со словарями:
my_dict = {'Kris': 1992, 'Masha': 1998, 'Kolya': 1991, 'Lesha': 1986}
print(my_dict)
print(my_dict.get('Kris'))
print(my_dict.get('Stepan'))
my_dict.update({'Semen': 1990, 'Ludvid': 2001})
a = my_dict.pop('Masha')
print(a)
print(my_dict)
#Работа с множествами
my_set = {1, 1, 2, 2, False, False, 'dub', 'dub', 'sosna', 'sosna'}
print(my_set)
my_set.add(5)
my_set.add('klen')
my_set.discard(1)
print(my_set)