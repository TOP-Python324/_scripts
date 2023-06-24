matrix1 = [
    [100, -200, 4],
    [4, -51, 63],
    [7, 8, 19],
]
matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


# переменная для аннотации
Matrix = list[list[float]]


def table_draw(
        matrix: Matrix, 
        *matrices: Matrix,
        padding: int = 8,
        vertical_sep: str = '|',
        horizontal_sep: str = '—',
        in_borders: bool = False,
        out_borders: bool = True
) -> str:
    """Формирует строку, содержащую горизонтальное табличное представление одной или нескольких матриц."""
    matrices = (matrix,) + matrices
    
    max_width = [
        max(len(str(n)) for row in matrix for n in row)
        for matrix in matrices
    ]
    # print(f'{max_width=}')
    
    vs = f' {vertical_sep} ' if in_borders else ' '

    # print(f'{vs=}')
    
    full_width = [
        len(matrix[0])*max_width[i] + len(vs)*(len(matrix[0]) - 1) + 2
        for i, matrix in enumerate(matrices)
    ]
    # print(f'{full_width=}')
    
    padding = ' '*padding
    lob = f'{vertical_sep} ' if out_borders else ' '
    rob = f' {vertical_sep}' if out_borders else ' '

    rows = []
    for i in range(len(matrix)):
        
        rows += [padding.join(
            lob + vs.join(
                f'{n:>{max_width[j]}}' 
                for n in matrix[i]
            ) + rob
            for j, matrix in enumerate(matrices)
        )]
        # print(f'{line=}')
    
    vertical_sep = vertical_sep if out_borders else ''
    h_line = padding.join(
        vertical_sep + horizontal_sep*width + vertical_sep
        for width in full_width
    )
    # print(f'{h_line=}')
    
    if in_borders:
        result = f'\n{h_line}\n'.join(rows)
    else:
        result = '\n'.join(rows)
    
    if out_borders:
        result = f'{h_line}\n{result}\n{h_line}'
    
    return result


print()
print(table_draw(matrix1, matrix2, matrix1, in_borders=False, out_borders=False), end='\n\n')
print(table_draw(matrix1, matrix2, matrix1, in_borders=False, out_borders=True), end='\n\n')
print(table_draw(matrix1, matrix2, matrix1, in_borders=True, out_borders=False), end='\n\n')
print(table_draw(matrix1, matrix2, matrix1, in_borders=True, out_borders=True), end='\n\n')
