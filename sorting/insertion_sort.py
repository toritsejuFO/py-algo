#!/usr/bin/python3

import util

def insertion_sort(array):
    # loop through entire array
    for i, item in enumerate(array):
        # skip first item (first item is already sorted)
        if (i == 0): continue

        # get the max index of sorted array
        sorted_i = i - 1

        # loop through sorted array backwards (from last to first)
        while sorted_i >= 0:
            # if item to be sorted is greater than/equal current item in sorted array,
            # item is already sorted, no swaps will eventually be made again
            # hence stop comparing other items in sorted array
            if item >= array[sorted_i]: break

            # perform swap if item to be sorted is less than current item in sorted array
            if item < array[sorted_i]:
                util.swap(i, sorted_i, array)
                i -= 1 # if swap is made, reduce index of item to be sorted
                sorted_i -= 1 # reduce index in sorted array to continue backwards search

    return array

if __name__ == '__main__':
    base_test_case = [8, 5, 2, 9, 5, 6, 3]
    print(insertion_sort(base_test_case))
