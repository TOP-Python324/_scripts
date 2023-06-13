ticket = input("Номер билета: ")
if int(ticket[0])+int(ticket[1])+int(ticket[2]) == int(ticket[3])+int(ticket[4])+int(ticket[5]):
    print("Да")
else:
    print("Нет")

#Номер билета: 153104
#Нет

#Номер билета: 171270
#Да

      