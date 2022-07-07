from roi.roi import User, Income, Expense, Investment, UserAlreadyExistsError
import unittest
from decimal import Decimal

incomes = [
    Income("income1", Decimal("1200.00")),
    Income("Income2", Decimal("500.123")),
    Income("Income3", Decimal("15500")),
]
expenses = [
    Expense("expense1", Decimal("100.15")),
    Expense("Expense2", Decimal("50.001")),
    Expense("Expense3", Decimal("300")),
]
investments = [
    Investment("Invest1", incomes, expenses, Decimal("155000")),
    Investment("Invest2", incomes, expenses, Decimal("15.000")),
    Investment("invest3", incomes, expenses, Decimal("20000.00")),
]


class TestUser(unittest.TestCase):
    def test_create_user(self):
        user1 = User("MattDubbz", investments)
        user2 = User("MattDubbz")
        user3 = User("Tony")
        self.assertIn(user1.username, User.usernames)
        self.assertNotIn("MattDubbz", User.usernames)
        self.assertIsNotNone(user1.investments)
        self.assertIn(investments[0], user1.investments)
        self.assertNotIn(investments[1], user3.investments)
        self.assertEqual(len(user3.investments), 0)
        self.assertEqual(len(user1.investments), 3)
        invest4 = Investment("invest4", incomes, expenses, Decimal("50000.00"))
        user1.add_investment(invest4)
        self.assertIn(invest4, user1.investments)
        user1.remove_investment(invest4)
        self.assertNotIn(invest4, user1.investments)
        uname = user3.get_username()
        self.assertEqual(uname, user3.username)
        self.assertEqual(uname, "tony")
        self.assertEqual(len(User.all_users), 3)
        self.assertIs(User.all_users[uname], user3)


class TestIncome(unittest.TestCase):
    def test_create_income(self):
        income1 = Income("income1", Decimal("1200.00"))
        income2 = Income("Income2", Decimal("500.123"))
        income3 = Income("Income3", Decimal("15500"))
        self.assertEqual(income1.amount, income1.get_amount())
        self.assertEqual(income2.amount, Decimal("500.12"))
        self.assertNotEqual(income2.amount, Decimal("500.123"))
        self.assertEqual(income3.amount, 15500)
        self.assertEqual(income3.get_amount(), 15500.00)
        self.assertNotEqual(income3.get_amount(), "15500")
        self.assertIsInstance(income3.get_amount(), Decimal)
        self.assertNotIsInstance(income3.get_amount(), str)
        self.assertNotIsInstance(income3.get_amount(), int)


class TestExpense(unittest.TestCase):
    def test_create_expense(self):
        expense1 = Expense("expense1", Decimal("100.15"))
        expense2 = Expense("Expense2", Decimal("50.001"))
        expense3 = Expense("Expense3", Decimal("300"))
        self.assertEqual(expense1.amount, expense1.get_amount())
        self.assertEqual(expense2.amount, Decimal("50.00"))
        self.assertNotEqual(expense2.amount, Decimal("50.001"))
        self.assertEqual(expense3.amount, 300)
        self.assertEqual(expense3.get_amount(), 300.00)
        self.assertNotEqual(expense3.get_amount(), "300")
        self.assertIsInstance(expense3.get_amount(), Decimal)
        self.assertNotIsInstance(expense3.get_amount(), str)
        self.assertNotIsInstance(expense3.get_amount(), int)


class TestInvestment(unittest.TestCase):
    def test_create_investment(self):
        invest1 = Investment("Invest1", incomes, expenses, Decimal("155000"))
        invest2 = Investment("Invest2", incomes, expenses, Decimal("15.000"))
        invest3 = Investment("invest3", incomes, expenses, Decimal("20000.00"))
        invest4 = Investment("invest4")
        self.assertEqual(invest1.name, "Invest1")
        self.assertNotEqual(invest1, "invest1")
        self.assertEqual(invest4.incomes, [])
        self.assertEqual(len(invest4.incomes), 0)
        self.assertEqual(len(invest1.incomes), 3)
        self.assertEqual(len(invest1.expenses), 3)
        income1 = Income("income1", Decimal("100.00"))
        income2 = Income("income2", Decimal("50000"))
        invest3.set_incomes(incomes=[income1, income2])
        self.assertEqual(len(invest3.incomes), 2)
        expense1 = Expense("expense1", Decimal("100.00"))
        expense2 = Expense("expense2", Decimal("50000"))
        invest3.set_expenses(expenses=[expense1, expense2])
        self.assertEqual(len(invest3.expenses), 2)
        self.assertEqual(invest4.get_incomes(), Decimal("0"))
        self.assertEqual(invest4.get_expenses(), Decimal("0"))
        invest4.set_total_invest("100500.00")
        self.assertEqual(invest4.get_total_invest(), Decimal("100500.00"))
        invest4.set_total_invest("100500.994")
        self.assertEqual(invest4.get_total_invest(), Decimal("100500.99"))
        self.assertEqual(invest4.get_total_invest(), invest4.total_invest)


if __name__ == "__main__":
    unittest.main()
