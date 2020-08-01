class Matrix:
    def __init__(self, i_list: list):
        """
        :param i_list: матрица - list
        """
        self.data = i_list

    # Наибольшее количество цифр в элементе матрицы для выравнивания при печати
    def __get_max_just(self):
        result = 1
        for y in self.data:
            for x in y:
                if len(str(x)) > result:
                    result = len(str(x))
        return result

    def __str__(self):
        max_just = self.__get_max_just()
        # Формирование строки для отображения матрицы в печатном виде
        result = ''
        for y in self.data:
            for x in y:
                result = result + str(x).rjust(max_just + 1)
            result = result + '\n'
        return result

    def __add__(self, other):
        result = []
        if len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
            # Поэлементное сложение
            for i in range(0, len(self.data)):
                temp_row = [x + y for x, y in zip(self.data[i], other.data[i])]
                result.append(temp_row)
            return Matrix(result)
        else:
            # Для матриц разной размерности операция сложения не определена
            raise ValueError


# Предполагается, что матрица передается по строкам
matrix1 = Matrix([[1.288, 2.54], [377, 4.1]])
matrix2 = Matrix([[100, 200], [300, 400]])
print('Результат сложения двух матриц:')
print(str(matrix1 + matrix2))
