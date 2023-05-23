#!/usr/bin/python3

import util

def selection_sort(array):
    # loop through entire "unsorted" array (reduces by 1 per loop)
    for i, _ in enumerate(array):
        selected = i # selected current index as the one with the smallest item

        # check to find an item smaller than the first (selected) item in unsorted array
        for j in range(i + 1, len(array)):
            if array[j] < array[selected]:
                selected = j

        # perform swap if a different smaller number was found
        if selected != i:
            util.swap(i, selected, array)
    
    return array

if __name__ == '__main__':
    base_test_case = [8, 5, 2, 9, 5, 6, 3]
    print(selection_sort(base_test_case))
