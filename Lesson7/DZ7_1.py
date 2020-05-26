class Matrix:
    def __init__(self, lst):
        self.lst = lst  # Принимает матрицу в виде списка списков (построчно).

    def __str__(self):
        matrix_for_print = ''
        for el in self.lst:
            matrix_for_print += ' '.join(map(str, el)) + '\n'
        return matrix_for_print

    def __add__(self, m2):
        sum_matrix = Matrix([])
        for i in range(len(self.lst)):
            sum_matrix.lst.append(list(map(sum, list(zip(self.lst[i], m2.lst[i])))))
        return sum_matrix


m = Matrix([[2, 3, 1], [4, 5, 6]])
n = Matrix([[1, 0, 0], [1, 1, 1]])
print(f"Первая матрица:\n{m}")
print(f"Вторая матрица:\n{n}")
print(f"Сумма матриц:\n{m + n}")
