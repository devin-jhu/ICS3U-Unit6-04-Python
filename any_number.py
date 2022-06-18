#!/usr/bin/env python3

# Created by Devin Jhu
# Created on June 2022
# The array average


import random


def calculations(number_array):
    # this function finds the average

    total = 0
    num_quantity = 0

    for counter_array in number_array:
        for number in counter_array:
            total += number
            num_quantity += 1

    average = total / num_quantity

    return average


def main():
    # this function generates a row/column array then outputs the average

    number_array = []
    
    # input
    try:
        rows = int(input("Enter rows: "))
        columns = int(input("Enter columns: "))
        print("")

        if rows <= 0 or columns <= 0:
            0 / 0  # causes crash if negative or zero

        # process & output
        for row_amount in range(0, rows):
            temp_array = []
            for columns_amount in range(0, columns):
                random_number = random.randint(1, 50)
                temp_array.append(random_number)
                print("{} ".format(random_number), end="")
            number_array.append(temp_array)
            print("")

        # call function
        average = calculations(number_array)

        # output
        print("\nThe average is {0:.2f}".format(average))

    except Exception:
        print("not a number")

    print("\nDone.")


if __name__ == "__main__":
    main()
