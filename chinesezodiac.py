"""
a program that prompts the user to enter a year
and displays the animal for the year.

"""


def chinese_year():
    year = int(input("Enter the year: "))
    years = {"monkey": 0, "rooster": 1, "dog": 2, "pig": 4, "rat": 4, "ox": 5, "tiger": 6, "rabbit": 7, "dragon": 8,
             "snake": 9, "horse": 10, "sheep": 11}
    key_list = list(years.keys())
    val_list = list(years.values())
    animals = year % 12
    position = val_list.index(animals)
    print(key_list[position])


chinese_year()
