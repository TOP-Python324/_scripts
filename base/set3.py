rus = ['Иванов', 'Петров', 'Козлов', 'Сергеев', 'Дмитриев']
math = ['Купринов', 'Ломов', 'Зырянов', 'Хайнуллин', 'Живов']
info = ['Молчунов', 'Хайнуллин', 'Баев', 'Шестов', 'Купринов']
bio = ['Злобнов', 'Царёв', 'Козлов', 'Жданов', 'Фомин']
geo = ['Бычков', 'Фомин', 'Сергеев', 'Чкалов', 'Живов']

olimps = {
    'русский язык': rus,
    'математика': math,
    'информатика': info,
    'биология': bio,
    'география': geo,
}

# all_students = set(rus) | set(math) | set(info) | set(bio) | set(geo)
all_students = set(rus + math + info + bio + geo)

all_students = {
    st: sum(st in ol for ol in olimps.values())
    for st in all_students
}


from itertools import combinations

# a b c
# ab ac bc

# a b c d
# ab ac ad bc bd cd 

for ol1, ol2 in combinations(olimps, 2):
    students = set(olimps[ol1]) & set(olimps[ol2])
    if students:
        print(f'{ol1} — {ol2}\n{", ".join(students)}\n')
    