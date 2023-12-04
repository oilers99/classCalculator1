class MyDefCalculator:
    """Класс калькулятор принимает 2 параметра
    Методы; Сложения Вычитание Умножение Деление"""

    def __init__(self, first, second):
        self.i_first = first
        self.i_second = second

    def addition(self):
        """Сложение"""
        result_addition = float(self.i_first) + float(self.i_second)
        print(f"Результат сложения {result_addition}")

    def subtraction(self):
        """Вычитание"""
        result_subtraction = float(self.i_first) - float(self.i_second)
        print(f"Результат вычитания {result_subtraction}")

    def multiplication(self):
        """умножение"""
        result_multiplication = float(self.i_first) * float(self.i_second)
        print(f"Результат умножения {result_multiplication}")

    def division(self):
        """Деление"""
        result_division = float(self.i_first) / float(self.i_second)
        print(f"Результат деления {result_division}")


class ExeputionTest(Exception):
    """
    Класс проверки введенных данных
    """

    def __init__(self, first_ex, second_ex, sign_ex):
        self.first_ex = first_ex
        self.second_ex = second_ex
        self.sign_ex = sign_ex

    def exeputin_test_in_digit(self):
        """проверка на цифры"""
        try:
            if self.first_ex.isdigit() and self.second_ex.isdigit():
                return True
        except Exception:
            return False

    def test_in_sign(self):
        """проверка на знак"""
        if self.sign_ex in ["/", "*", "+", "-"]:
            return True
        else:
            print(f"Вы ввели недопустимый знак '{self.sign_ex}'")


def calculator(first, second, sign):
    """
    По заданному знаку вызывает соответств метод в Классе
    MyDefCalculator
    """
    test_in_digit = ExeputionTest(first, second, sign)
    if test_in_digit.exeputin_test_in_digit():
        if test_in_digit.test_in_sign():
            result = MyDefCalculator(first, second)
            if sign == "+":
                result.addition()
            elif sign == "-":
                result.subtraction()
            elif sign == "*":
                result.multiplication()
            elif sign == "/":
                result.division()
    else:
        print(f"БукавЫ блять!!! {first}, {second}")


if __name__ == "__main__":
    calculator(input("Введите первое число "),
               input("Введите второе число "),
               input("Введтие знак "))
