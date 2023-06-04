(word := 'expression')

# многоуровенвая инструкция
n1 = n2 = 1
# синтаксический сахар для 
n2 = 2
n1 = 2

# одноуровневая инструкция присвоения с выражением в правом операнде
n1 = (n2 := 3)


numbers = []
while (inp := input()):
    if inp.isdecimal():
        numbers += [int(inp)]

