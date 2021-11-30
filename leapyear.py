"""
Determining Leap Year
"""


def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return print("This year is  Leap")
    else:
        return print("This is not a Leap Year")


years = int(input("Enter the Year: "))
leap_year(years)
