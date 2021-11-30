def multiplication_table():
    # a = int(input("enter a number: "))
    b = 1
    for i in range(0, 10):
        for b in range(0, 10):
            c = b * i
            print("{} * {} =".format(i, b), c)


multiplication_table()
