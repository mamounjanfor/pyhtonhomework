import random

"""
Now let us consider how to generate a random lowercase letter. The ASCII
code for lowercase letters are consecutive integers starting from the ASCII
code for 'a', then for 'b', 'c', ..., and 'z'. The ASCII code for 'a' is
ord('a')

❑ So, a random integer between ord('a') and ord('z') is

random.randint(ord('a'), ord('z'))
❑ And, a random lowercase letter is

chr(random.randint(ord('a'), ord('z')))

❑ To generalize the foregoing discussion, a random character between any two
characters ch1 and ch2 with ch1 < ch2 can be generated as follows:
chr(random.randint(ord(ch1), ord(ch2)))
"""


def generate_random_character():
    return print(chr(random.randint(ord("a"), ord("z"))))


def total_two_numbers():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    print(a)
    print(b)
    c = a + b
    answer = int(input("Enter the total of the two numbers: "))
    if c == answer:
        print("You are right!")
    else:
        print("Wrong answer")


def calculate_bmi(weight, height):

    bmi = weight/(height**2)
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25.0:
        print("Normal")
    elif 25.0 <= bmi < 30.0:
        print("Overweight")
    else:
        print("Obese")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    generate_random_character()
    total_two_numbers()

    weights = int(input("Enter your Weight in Kg: "))
    heights = float(input("Enter your Height in Meters: "))
    calculate_bmi(weights, heights)
