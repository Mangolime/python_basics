class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, cell):
        return Cell(self.number + cell.number)

    def __sub__(self, cell):
        if self.number - cell2.number > 0:
            return Cell(self.number - cell.number)
        else:
            print("Во второй клетке количество ячеек не меньше чем в первой")

    def __mul__(self, cell):
        return Cell(self.number * cell.number)

    def __truediv__(self, cell):
        return Cell(self.number // cell.number)

    def make_order(self, col):
        fraction = self.number // col
        excess = self.number % col
        return ('*' * col + '\n') * fraction + '*' * excess


cell1 = Cell(13)
cell2 = Cell(6)
print(f"Первая клетка:\n{cell1.make_order(4)}")
print(f"Вторая клетка:\n{cell2.make_order(4)}")
print("Сложение клеток:", (cell1 + cell2).number)
print("Вычитание клеток:", (cell1 - cell2).number)
print("Умножение клеток:", (cell1 * cell2).number)
print("Деление клеток:", (cell1 / cell2).number)
