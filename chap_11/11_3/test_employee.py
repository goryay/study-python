import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        """Создаем экземпляр Employee для использования в тестах"""
        self.employee = Employee("Иван", "Иванов", 50000)

    def test_give_default_raise(self):
        """Тест на проверку повышения с использованием стандартного процента"""
        default_raise_percent = 0.05  # Стандартное повышение на 5%
        expected_salary = self.employee.salary * (1 + default_raise_percent)

        self.employee.give_raise(default_raise_percent)
        self.assertEqual(self.employee.salary * (1 + default_raise_percent), expected_salary)

    def test_give_custom_raise(self):
        """Тест на проверку повышения с использованием пользовательского процента"""
        custom_raise_percent = 0.1  # Повышение на 10%
        expected_salary = self.employee.salary * (1 + custom_raise_percent)

        self.employee.give_raise(custom_raise_percent)
        self.assertEqual(self.employee.salary * (1 + custom_raise_percent), expected_salary)
