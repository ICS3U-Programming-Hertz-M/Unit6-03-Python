#!/usr/bin/env python3

# Created by: Sarah
# Created on: May 28th, 2022.
# this program Generates 10 random numbers from 0-100 and displays
# the min value to the user.
import constants
import random


def find_min_value(arrays_num):
    min_value = 101
    min_value = arrays_num[0]

    # determines the min value
    for a_num in arrays_num:
        if a_num < min_value:
            min_value = a_num

    return min_value


def main():
    # initialize counter and create an empty list
    counter = 0
    random_num = []

    # generates a range of random numbers
    for counter in range(constants.MAX_ARRAY_SIZE):
        random_num.append(random.randint(constants.MIN_N, constants.MAX_N))

        # displays the numbe added and it's position.
        print("{} is added to the list at position {}"
              .format(random_num[counter], counter))

    # call function & display the min value to the user
    minimum = find_min_value(random_num)
    print("")
    print("{} is the lowest value(min value)".format(minimum))


if __name__ == "__main__":
    main()
