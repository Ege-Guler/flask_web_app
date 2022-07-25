import sympy as sym
sym.init_printing(use_unicode=True)

#fm as first matrix
#sm as second matrix

#first_matrix and second_matrix are inputs

first_matrix = [[1,2]]
second_matrix = [[1],[2]]

fm = sym.Matrix(first_matrix)
sm = sym.Matrix(second_matrix)

try:
    result = fm * sm
    print(result)

except sym.ShapeError:
    print("retry")
    



