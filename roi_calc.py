from roi.roi import User, Income, Expense, Investment, UserAlreadyExistsError


def display_menu():
    print("=" * 30)
    print("[1]\tSelect User")
    print("[2]\tCreate an Investment")
    print("[3]\tDelete an Investment")
    print("[4]\tView an Investment")
    print("[5]\tEdit an Investment")
    print("[6]\tExit Program.")
    print("=" * 30)


def get_input():
    choice = ""
    while not isinstance(choice, int):
        try:
            choice = int(input("Enter your choice here: "))
        except Exception as e:
            print(e)
            print("Try again and enter a numeric option.")
    return choice


def choose_user():
    print("=" * 79)
    print("Usernames will all be converted to lowercase.")
    try:
        username = input(
            "Type the username you want to choose. If it doesn't exist, it will be created: "
        )
        if username in User.all_users:
            print(f"Selected user {username}")
            return User.all_users[username]
        else:
            user = User(username)
    except UserAlreadyExistsError as e:
        print(e.message)

    print("That username has not yet been taken. It's yours.")
    print("=" * 79)
    return user


def get_incomes():
    print("=" * 79)
    print("All incomes are entered as monthly incomes")
    incomes = []
    done = False
    while not done:
        name = input("Enter the name for this stream of income: ").title()
        amount = input("Enter the amount for this stream of income: ")
        income = Income(name, amount)
        incomes.append(income)
        choice = input(
            "Press (y/Y) to enter another income stream for this investment: "
        )
        print("=" * 79)
        if choice.lower() != "y":
            done = True
    return incomes


def get_expenses():
    print("=" * 79)
    print("All expenses are entered as monthly expenses.")
    expenses = []
    done = False
    while not done:
        name = input("Enter the name for this expense: ").title()
        amount = input("Enter the amount for this expense: ")
        expense = Expense(name, amount)
        expenses.append(expense)
        choice = input("Press (y/Y) to enter another expense for this investment: ")
        print("=" * 79)
        if choice.lower() != "y":
            done = True
    return expenses


def create_investment(user):
    print("=" * 79)
    name = input("Enter the name of the investment: ").title()
    print("Next is incomes for the investment.")
    incomes = get_incomes()
    print("Next is expenses for the investment.")
    expenses = get_expenses()
    total_invest = input(
        "Enter the total amount of money you have put into the investment: "
    )
    investment = Investment(name, incomes, expenses, total_invest)
    user.add_investment(investment)
    print(f"The {name} investment has been added.")
    print("=" * 79)


def delete_investment(user):
    print("=" * 79)
    print("This option will remove a investment from your portfolio.")
    name = input("Enter the name of investment you want to remove: ").title()
    if len(user.investments) == 0:
        print(f"There are no investments for {user}.")
    for invest in user.investments:
        if name == invest.name:
            user.remove_investment(invest)
            print(f"{name} investment has been removed.")
        else:
            print("An investment by that name was not found.")
    print("=" * 79)


def view_investment(user):
    print("=" * 79)
    print("This will show you all the info on your investment.")
    name = input("Enter the name of investment you want to view: ").title()
    if len(user.investments) == 0:
        print(f"There are no investments for {user}.")
    for invest in user.investments:
        if name == invest.name:
            print(f"Investment Name: {invest.name}:")
            print(f"{invest.name} income streams:")
            for income in invest.incomes:
                print(f"\tIncome {income.name}, Amount: {income.amount}.")
            for expense in invest.expenses:
                print(f"\tExpense {expense.name}, Amount: {expense.amount}.")
            print(f"Total income is {invest.total_income}.")
            print(f"Total Expense is {invest.total_expense}.")
            print(f"Cash Flow is {invest.cash_flow}.")
            print(f"Annual Cash Flow is {invest.annual_cash_flow}.")
            print(f"ROI is {invest.roi}.")
        else:
            print("An investment by that name was not found.")
    print("=" * 79)


def edit_investment(user):
    print("=" * 79)
    print("This will allow you to edit an investment.")
    print("You will re-enter all relevent data for the investment.")
    name = input("Enter the name of investment you want to edit: ").title()
    if len(user.investments) == 0:
        print(f"There are no investments for {user}.")
    for invest in user.investments:
        if name == invest.name:
            name = input("Enter the new name for the investment: ").title()
            invest.set_name(name)
            print("Enter the new incomes and expenses for this investment")
            incomes = get_incomes()
            expenses = get_expenses()
            invest.set_incomes = incomes
            invest.set_expenses(expenses)
            total_invest = input(
                "Enter the total amount of money you have put into the investment: "
            )
            invest.set_total_invest(total_invest)
            print(
                "All data has been updated including cash flow, annual cash flow, and ROI."
            )
        else:
            print("An investment by that name has not been found.")
    print("=" * 79)


print("This is ROI-CALC.")
done = False
user = choose_user()
while not done:
    display_menu()
    choice = get_input()
    while choice < 1 or choice > 6:
        print("Enter 1 - 7 only.")
        choice = get_input()
    if choice == 1:
        username = choose_user()
    elif choice == 2:
        create_investment(user)
    elif choice == 3:
        delete_investment(user)
    elif choice == 4:
        view_investment(user)
    elif choice == 5:
        edit_investment(user)
    elif choice == 6:
        print("Shutting down.")
        done = True
print("Thank you come again.")
