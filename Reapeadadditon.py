import random

"""
Recall the Simple Math Tool program from previous
module that prompts the student to enter an answer
for a question on addition of two single digit integers.
"""


def cal_two():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    print(a)
    print(b)
    c = a + b

    while True:
        d = int(input("Enter you answer: "))
        if c == d:
            print("Correct")
            break
        else:
            print("Try again")


cal_two()
