matrix1 = [
    [100, -200, 4],
    [4, -51, 63],
    [7, 8, 19],
]

max_width1 = max(len(str(n)) for row in matrix1 for n in row) + 1
v_sep = '|'
h_sep = '—'
full_width = len(matrix1[0]) * (max_width1 + 1) + len(v_sep) * (len(matrix1[0]) + 1)
hor_line = h_sep*full_width

# for row in matrix1:
    # print(' | '.join(str(n).rjust(max_width1, '_') for n in row))

table = f'{hor_line}\n' + f'\n{hor_line}\n'.join(
    v_sep + v_sep.join(f'{n:>{max_width1}} ' for n in row) + v_sep
    for row in matrix1
) + f'\n{hor_line}'
print(table)

print()


matrix2 = [list(range(n, n+10)) for n in range(1, 101, 10)]

max_width2 = max(len(str(n)) for row in matrix2 for n in row)

for row in matrix2:
    print(' '.join(f'{n:_<{max_width2}}' for n in row))
    # print(' '.join(str(n).ljust(max_width2, '_') for n in row))
print()

