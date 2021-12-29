class Category:
    # Variables
    def __init__(self, budget):
        self.budgetCategories = budget
        self.withdrawed = 0
        self.balance = 0
        self.ledger = []

    def deposit(self, amt, description=""):

        self.balance += amt
        self.ledger.append({"amount": amt, "description": description})

    def withdraw(self, amt, description=""):
        if not self.check_funds(amt):
            return False
        else:

            self.ledger.append({"amount": -amt, "description": description})
            self.balance -= amt
            self.withdrawed += amt
            return True

    def get_balance(self):
        return self.balance

    def transfer(self, amt, category):
        if not self.check_funds(amt):
            return False
        else:
            self.withdraw(
                amt, "Transfer to {category}".format(category=category.budgetCategories)
            )
            category.deposit(
                amt, "Transfer from {category}".format(category=self.budgetCategories)
            )
            return True

    def check_funds(self, amt):
        if amt > self.balance:
            return False
        else:
            return True

    def __repr__(self):
        title = (
            "*" * int(30 / 2 - len(self.budgetCategories) // 2) + self.budgetCategories
        )
        title += (30 - len(title)) * "*" + "\n"
        itemsAndAmt = ""

        for item in self.ledger:
            # print(item["description"][0:23])
            itemDescription = item["description"][0:23]
            # print(len(itemsAndAmt))
            # print(itemsAndAmt)
            amountInNumber = "{:0.2f}".format(item["amount"])[0:7]
            # print(len(amountInNumber))
            whiteSpaces = 30 - len(itemDescription) - len(amountInNumber)

            print(whiteSpaces)
            itemsAndAmt += itemDescription + whiteSpaces * " " + amountInNumber + "\n"
            # print(itemsAndAmt)

        itemsAndAmt += "Total: " + "{:0.2f}".format(self.balance)[0:7]
        return title + itemsAndAmt


def getMaxLen(categories):
    budget = []
    for category in categories:
        budget.append(len(category.budgetCategories))
    # print(budget)
    return max(budget)


def create_spend_chart(categories):
    percentage = []
    totalWithdraw = 0

    for category in categories:
        totalWithdraw += category.withdrawed

    for category in categories:
        p = int((category.withdrawed / totalWithdraw) * 100)
        if (p % 10) < 5:
            p -= p % 10
        elif (p % 10) >= 5:
            p += 10 - p % 10

        percentage.append(p)

    res = "Percentage spent by category\n"

    for i in range(0, 11):
        number = 100 - i * 10
        res = res + (3 - len(str(number))) * " " + str(number) + "| "

        for p in percentage:
            if p >= number:
                res = res + "o" + "  "
            else:
                res = res + " " * 3

        res += "\n"

    res = res + " " * 4 + (3 * len(categories) + 1) * "-" + "\n"  # ------------

    maxLenBudget = getMaxLen(categories)
    # for i in range(len(categories)):
    #   res += ' ' * 5
    #   for j in range(len(maxLenBudget)):

    # problem here
    for i in range(maxLenBudget):
        res += " " * 5
        for category in categories:

            if i < len(category.budgetCategories):
                res += category.budgetCategories[i]
            else:
                res += " "
            res += " " * 2
            if category == categories[-1]:
                res += "\n"
    return res
