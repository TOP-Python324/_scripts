mammals = {
    'тигр',
    'верблюд',
    'баран',
    'кит',
    'морж',
}
aquatic = {
    'осьминог',
    'креветка',
    'краб',
    'кит',
    'морж',
}

print(f'{mammals | aquatic = }')
print(f'{mammals & aquatic = }')
print(f'{mammals - aquatic = }')
print(f'{aquatic - mammals = }')
print(f'{aquatic ^ mammals = }\n')
# print(f'{(aquatic | mammals) - (mammals & aquatic) = }')

reptiles = {
    'черепаха',
    'ящерица',
    'змея',
    'крокодил',
}

print(f'{mammals.isdisjoint(aquatic) = }')
# print(f'{aquatic.isdisjoint(mammals) = }')
print(f'{mammals.isdisjoint(reptiles) = }\n')
# print(f'{reptiles.isdisjoint(mammals) = }\n')

aquatic_mammals = {'кит', 'морж'}

print(f'{mammals > aquatic_mammals = }')
# print(f'{aquatic_mammals < mammals = }')
print(f'{mammals > aquatic = }\n')
# print(f'{aquatic < mammals = }\n')

a = {1, 2, 3}
b = {1, 2, 3}
print(f'{a < b = }')
print(f'{a <= b = }')
