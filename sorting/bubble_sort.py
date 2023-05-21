#!/usr/bin/python3

import util

def bubble_sort(array):
    i = 0
    i_max_iter = len(array) - 1
    shouldBubble = True

    while shouldBubble:
        shouldBubble = False
        for i in range(i_max_iter):
            if array[i] > array[i+1]:
                util.swap(i, i + 1, array)
                shouldBubble = True
        i_max_iter -= 1   

    return array

if __name__ == '__main__':
    base_test_case = [8, 5, 2, 9, 5, 6, 3]
    print(bubble_sort(base_test_case))
