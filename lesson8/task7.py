class ComplexNumber:
    def __init__(self, real, imaginary):
        """
        :param real: действительная часть числа
        :param imaginary: мнимая часть числа
        """
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary+other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.real * other.imaginary + self.imaginary * other.real)

    def __str__(self):
        return str(self.real) + ('-' if self.imaginary < 0 else '+') + str(abs(self.imaginary)) + 'i'


complex1 = ComplexNumber(1, 2)
complex2 = ComplexNumber(5, -3)
print('Результат сложения комплексных чисел:')
print(str(complex1) + ' + ' + str(complex2) + ' = ' + str(complex1 + complex2))
print('Результат умножения комплексных чисел:')
print(str(complex1) + ' * ' + str(complex2) + ' = ' + str(complex1 * complex2))

# то же самое с помощью встроенной функции для проверки
# complex1 = complex(1, 2)
# complex2 = complex(5, -3)
# print('Результат сложения комплексных чисел:')
# print(str(complex1) + ' + ' + str(complex2) + ' = ' + str(complex1 + complex2))
# print('Результат умножения комплексных чисел:')
# print(str(complex1) + ' * ' + str(complex2) + ' = ' + str(complex1 * complex2))

