students = [
    'Башлыков Александр Владимирович', 
    'Бушкин Владислав Вячеславович', 
    'Варваров Артём Денисович', 
    'Григорьев Константин Александрович', 
    'Жильцов Александр Владимирович', 
    'Кабаргин Марк Денисович', 
    'Калеров Алексей Игорьевич', 
    'Котляров Артур Сергеевич', 
    'Мареев Дмитрий Александрович', 
    'Оргеткин Никита Викторович', 
    'Раецкая Валерия Николаевна', 
    'Тепляков Владислав Алексеевич', 
    'Устинов Алексей Николаевич'
]

print(id(students))

students[0] = students[0].split(' ')[0]
students[1] = students[1].split(' ')[0]
students[2] = students[2].split(' ')[0]
students[3] = students[3].split(' ')[0]
students[4] = students[4].split(' ')[0]
students[5] = students[5].split(' ')[0]
students[6] = students[6].split(' ')[0]
students[7] = students[7].split(' ')[0]
students[8] = students[8].split(' ')[0]
students[9] = students[9].split(' ')[0]
students[10] = students[10].split(' ')[0]
students[11] = students[11].split(' ')[0]
students[12] = students[12].split(' ')[0]

print(id(students))

print(students)
