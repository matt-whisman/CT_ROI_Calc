from decimal import Decimal


class UserAlreadyExistsError(Exception):
    """Custom exception for when a username is already contained in the User.usernames class attribute list.

    Raises:
        UserAlreadyExistsError: username is already in User.usernames"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = "That username already exists."


class User:
    """Create a User with a unique username and a list of their investments.

    Keyword arguments:
    username -- a unique username
    investments -- a list of Investments objects
    Return: None
    """

    """class attribute list for all usernames"""

    usernames = []
    all_users = {}

    def __init__(self, username, investments=None):
        try:
            if username.lower() not in self.usernames:
                # self.usernames.append(username.lower())
                self.username = username.lower()
            else:
                raise UserAlreadyExistsError(username)
        except Exception as e:
            print(e)

        if investments is None:
            self.investments = []
        else:
            self.investments = investments

        # add the object to a dict of all objects with the username as the key
        User.all_users[username] = self

    def __str__(self) -> str:
        return self.username

    """Adds an Investment object to the users list of investments.

    Keyword arguments:
    investment -- An Investment object
    Return: None
    """

    def add_investment(self, investment):
        self.investments.append(investment)

    """Delete an Investment of the user.

    Keyword arguments:
    investment -- An Investment of the user to delete.
    Return: None
    """

    def remove_investment(self, investment):
        if investment in self.investments:
            self.investments.remove(investment)

    """Get and return a User's Investment object

    Keyword arguments:
    investment -- A User's Investment object.
    Return: Investment object if it exists, otherwise returns None.
    """

    def get_investment(self, investment):
        if investment in self.investments:
            return investment
        else:
            return None

    """Return the User's username attribute.

    Keyword arguments:
    argument -- No args
    Return: User's username attribute.
    """

    def get_username(self):
        return self.username


class Income:
    """Income represents a single stream or source of income that comes from an investment."""

    """Creates an Income object used in an Investment.

    Keyword arguments:
    name -- String name of the stream of income.
    amount -- String dollar amount of the income.
    Return: None
    """

    def __init__(self, name: str, amount: str) -> None:
        self.name = name
        self.amount = Decimal(amount).quantize(Decimal("1.00"))

    def get_name(self):
        return self.name

    # returns Decimal object
    def get_amount(self):
        return self.amount

    def set_name(self, name: str):
        self.name = name

    def set_amount(self, amount: str):
        self.amount = Decimal(amount).quantize(Decimal("1.00"))


class Expense:
    """Expense represents a single expense for an investment.

    Keyword arguments:
    name -- String name of the expense.
    amount -- String dollar amount of the expense.
    Return: None
    """

    def __init__(self, name: str, amount: str) -> None:
        self.name = name
        self.amount = Decimal(amount).quantize(Decimal("1.00"))

    def get_name(self):
        return self.name

    # returns a Decimal object
    def get_amount(self):
        return self.amount

    def set_name(self, name: str):
        self.name = name

    def set_amount(self, amount: str):
        self.amount = Decimal(amount).quantize(Decimal("1.00"))


class Investment:
    """An Investment or property and it's attributes including Incomes and Expenses along with other calculations.

    Keyword arguments:
    name -- Name of the investment or property.
    incomes -- List of the Incomes that come from the investment.
    expenses -- List of the Expenses that come from the investment.
    total_invest -- The total amount of money that went into the investment used for calculating ROI. Entered as a string and converted to a Decimal type.
    Return: None
    """

    def __init__(
        self, name: str, incomes=None, expenses=None, total_invest="0"
    ) -> None:
        self.name = name
        # check the contents of the lists passed in
        if incomes is None:
            self.incomes = []
        else:
            self.incomes = incomes
        if expenses is None:
            self.expenses = []
        else:
            self.expenses = expenses
        # round based on value of total_invest to two decimal places.
        self.total_invest = Decimal(total_invest).quantize(Decimal("1.00"))

        # get total incomes and expenses
        income_count = Decimal("0")
        if len(self.incomes) > 0:
            for income in incomes:
                income_count += income.amount
        self.total_income = income_count.quantize(Decimal("1.00"))

        expense_count = Decimal("0")
        if len(self.incomes) > 0:
            for expense in expenses:
                expense_count += expense.amount
        self.total_expense = expense_count

        # set cash flow (I-E)
        if len(self.incomes) > 0:
            self.cash_flow = self.total_income - self.total_expense
        else:
            self.cash_flow = Decimal("0")

        # set annual cash flow to cash_flow * 12
        self.annual_cash_flow = self.cash_flow * Decimal("12.00")
        self.annual_cash_flow = self.annual_cash_flow.quantize(Decimal("1.00"))

        # set ROI to annual_cash_flow / total_invest
        if self.annual_cash_flow > 0:
            self.roi = self.annual_cash_flow / self.total_invest
            self.roi = self.roi.quantize(Decimal("1.00"))

        else:
            self.roi = Decimal("0")

    """Set the Incomes for the Investment.

    Keyword arguments:
    incomes -- List of Income objects for all incomes for the Investment.
    Return: None. If no Incomes are passed in, method has no effect.
    """

    def set_incomes(self, incomes=None):
        if incomes is not None:
            self.incomes = incomes

        # update the total_income with the new Incomes
        income_count = Decimal("0")
        if len(self.incomes) > 0:
            for income in self.incomes:
                income_count += income.amount
        self.total_income = income_count

        # update the cash_flow
        if len(self.incomes) > 0:
            self.cash_flow = self.total_income - self.total_expense
        else:
            self.cash_flow = Decimal("0")

        # update annual_cash_flow
        self.annual_cash_flow = self.cash_flow * Decimal("12.00")
        self.annual_cash_flow = self.annual_cash_flow.quantize(Decimal("1.00"))

        # update roi
        if self.annual_cash_flow > 0:
            self.roi = self.annual_cash_flow / self.total_invest
            self.roi = self.roi.quantize(Decimal("1.00"))
        else:
            self.roi = Decimal("0")

    """Gets all the Incomes for the Investment

    Keyword arguments:
    None
    Return: List of Incomes, Decimal("0") if there are no Incomes.
    """

    def get_incomes(self):
        if len(self.incomes) > 0:
            return self.incomes
        else:
            return Decimal("0")

    """Set the Expenses for the Investment

    Keyword arguments:
    expenses -- List of Expenses.
    Return: None. If no Expenses are passed in, method has no effect.
    """

    def set_expenses(self, expenses=None):
        if expenses is not None:
            self.expenses = expenses

        # update the total_expense with the new Expenses
        expense_count = Decimal("0")
        if len(self.incomes) > 0:
            for expense in expenses:
                expense_count += expense.amount
        self.total_expense = expense_count

        # update the cash_flow
        if len(self.incomes) > 0:
            self.cash_flow = self.total_income - self.total_expense
        else:
            self.cash_flow = Decimal("0")

        # update annual_cash_flow
        self.annual_cash_flow = self.cash_flow * Decimal("12.00")
        self.annual_cash_flow = self.annual_cash_flow.quantize(Decimal("1.00"))

        # update roi
        if self.annual_cash_flow > 0:
            self.roi = self.annual_cash_flow / self.total_invest
            self.roi = self.roi.quantize(Decimal("1.00"))
        else:
            self.roi = Decimal("0")

    """Get all Expenses for the Investment.

    Keyword arguments:
    None
    Return: List of Expenses, Decimal("0") if there are no Expenses.
    """

    def get_expenses(self):
        if len(self.expenses) > 0:
            return self.expenses
        else:
            return Decimal("0")

    """Set the name of the Investment.

    Keyword arguments:
    name -- Name label of the investment.
    Return: None
    """

    def set_name(self, name):
        self.name = name

    """Get the name of the Investment

    Keyword arguments:
    None
    Return: String name of the Investment
    """

    def get_name(self):
        return self.name

    """Set the total investment into the Investment

    Keyword arguments:
    total_invest -- Dollar amount of the total investment into the Investment or property.
    Return: None
    """

    def set_total_invest(self, total_invest):
        self.total_invest = Decimal(total_invest).quantize(Decimal("1.00"))

        # update roi
        self.roi = self.annual_cash_flow / self.total_invest
        self.roi = self.roi.quantize(Decimal("1.00"))

    """Get the total investment into the Investment.

    Keyword arguments:
    None
    Return: total_invest of the Investment.
    """

    def get_total_invest(self):
        return self.total_invest
