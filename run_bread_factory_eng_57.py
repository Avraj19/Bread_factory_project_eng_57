# print('2 truck in the distance, a gard get up and directs them')
# water_truck = input('you drive a water truck drive, what did you brings in your truck?')
from function_bread_factory_eng_57 import *
# test 1
print('When make_dough is called with \'water\' and \'flour\' it should return dough')
print(make_dough('water', 'flour') == 'dough')
print('got:', make_dough('water', 'flour'), '\n')

# test 2 - make_dough()
print('When make_dough is called with \'water\' and \'cement\' it shoulf return \'NOT dough\'')
print(make_dough('water', 'cement') == 'NOT dough')
print('got:', make_dough('water', 'cement'), '\n')

# test 3 - bake_bread
print("When bake_bread is called with 'dough' it should return 'bread'")
print(bake_bread('dough') == 'bread')
print('got:', bake_bread('dough'), '\n')

# test 4 - make_wheat_dough
print('When make_wheat_bread is called with \'water\' and \'wholewheat flour\' it should return dough')
print(make_wheat_dough('water', 'wholewheat flour') == 'Wholewheat dough')
print('got:', make_wheat_dough('water', 'wholewheat flour'), '\n')

# test 5 - make_wheat_bread
print("When make_wheat_bread is called with 'Wholewheat dough' it should return 'Wholewheat bread'")
print(make_wheat_bread('Wholewheat dough') == 'Wholewheat bread')
print('got:', make_wheat_bread('Wholewheat dough'), '\n')