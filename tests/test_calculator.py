import pytest

from app.calculator import Calculator

class TestCalc:

    def setup(self):
        # инициализируем приложение калькулятор
        self.calculator = Calculator

    def test_adding_success(self):
        # проверяем работу сложения
        assert self.calculator.adding(self, 3, 4) == 7

    def test_subtraction_success(self):
        # проверяем работу вычитания
        assert self.calculator.subtraction(self, 5, 3) == 2

    def test_multiply_success(self):
        # проверяем работу умножения
        assert self.calculator.multiply(self, 2, 7) == 14

    def test_division_success(self):
        # проверяем работу деления
        assert self.calculator.division(self, 9, 3) == 3

    def test_zero_division(self):
        # проверяем деление на ноль, выкидываем исключение
        with pytest.raises(ZeroDivisionError):
            self.calculator.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')


