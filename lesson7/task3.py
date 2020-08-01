class Cell:
    def __init__(self, number_of_cells: int):
        """
        :param number_of_cells: количество ячеек в клетке - int
        """
        if number_of_cells > 0:
            self.number_of_cells = number_of_cells
        else:
            raise ValueError

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        diff = self.number_of_cells - other.number_of_cells
        if diff > 0:
            return Cell(diff)
        else:
            print('Невозможно создать ячейку')

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __truediv__(self, other):
        # Автор задачи путается в показаниях:
        # сначала написано "В методе деления должно осуществляться округление значения до целого числа",
        # а затем "Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток".
        # Я считаю, что в этой задаче правильно использовать целочисленное деление
        return Cell(self.number_of_cells // other.number_of_cells)

    def make_order(self, cells_in_row: int):
        """
        :param cells_in_row: количество ячеек в ряду - int
        """
        result = ''
        idx = 0
        while idx < self.number_of_cells // cells_in_row:
            if result:
                result += '\n'
            result += '*' * cells_in_row
            idx += 1
        if self.number_of_cells % cells_in_row != 0:
            if result:
                result += '\n'
            result += '*' * (self.number_of_cells % cells_in_row)
        return result


cell1 = Cell(21)
cell2 = Cell(4)
print('Результат сложения: ' + str((cell1 + cell2).number_of_cells))
print('Результат вычитания: ' + str((cell1 - cell2).number_of_cells))
print('Результат вычитания: ' + str(cell2 - cell1))
print('Результат умножения: ' + str((cell1 * cell2).number_of_cells))
print('Результат деления: ' + str((cell1 / cell2).number_of_cells))
print('Ячейки по рядам:\n' + cell1.make_order(5))



