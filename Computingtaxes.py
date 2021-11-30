"""
The US federal personal income tax is calculated based
on the filing status and taxable income. There are four
filing statuses: single filers, married filing jointly, married
filing separately, and head of household. The tax rates
for 2009 are shown below.

"""


def compute_tax():
    status = int(input(
        "Enter you status, [0] for single, [1] for married filling jointly or widow, [2] for married filling separately, [3] head of household: "))
    income = int(input("Enter your income: "))
    if (status == 0 and 0 <= income <= 8350) or (status == 1 and 0 <= income <= 16700) or (
            status == 2 and 0 <= income <= 8350) or (status == 3 and 0 <= income <= 11950):
        tax = (income * 10) / 100
        print("your income tax is {}".format(tax))
    elif (status == 0 and 8351 <= income <= 33950) or (status == 1 and 16701 <= income <= 67900) or (
            status == 2 and 0 <= income <= 8350) or (status == 3 and 11951 <= income <= 45500):
        tax = (income * 15) / 100
        print("your income tax is {}".format(tax))
    elif (status == 0 and 33951 <= income <= 82250) or (status == 1 and 67901 <= income <= 137050) or (
            status == 2 and 33951 <= income <= 68525) or (status == 3 and 45501 <= income <= 117450):
        tax = (income * 25) / 100
        print("your income tax is {}".format(tax))
    elif (status == 0 and 82521 <= income <= 171550) or (status == 1 and 137051 <= income <= 208850) or (
            status == 2 and 68526 <= income <= 104425) or (status == 3 and 117451 <= income <= 190200):
        tax = (income * 28) / 100
        print("your income tax is {}".format(tax))
    elif (status == 0 and 171551 <= income <= 372950) or (status == 1 and 208851 <= income <= 372950) or (
            status == 2 and 104426 <= income <= 186475) or (status == 3 and 190201 <= income <= 372950):
        tax = (income * 33) / 100
        print("your income tax is {}".format(tax))
    elif ((status == 0 or status == 1 or status == 3) and 372951 <= income) or (status == 2 and 186476 <= income):
        tax = (income * 25) / 100
        print("your income tax is {}".format(tax))


compute_tax()
