#!/usr/bin/env python

import math

unsorted_list = [3, 8, 2, 5, 1, 4, 7, 6]


comparison_counter = 0


def quick_sort(input_list):
    global comparison_counter
    if len(input_list) <= 1:
        return input_list
    else:
        comparison_counter += len(input_list) - 1
        determine_median(input_list)
        pivot = input_list[0]
        i = 1
        j = 1
        for _ in range(len(input_list)-1):
            if input_list[j] > pivot:
                j += 1
            else:
                swap_elements(input_list, i, j)
                i += 1
                j += 1
        input_list = swap_elements(input_list, 0, i - 1)
        left = quick_sort(input_list[:i-1])
        right = quick_sort(input_list[i:])
        input_list = left + [input_list[i-1]] + right
        return input_list


def determine_median(input_list):
    # mid_index gives the middle index of the list, rounding down for lists of even length
    mid_index = math.floor((len(input_list) - 1) / 2)
    # mid_value gives the middle element of the list
    mid_value = input_list[mid_index]
    minv = min(input_list[0], input_list[-1])
    maxv = max(input_list[0], input_list[-1])
    if mid_value < minv:
        return swap_elements(input_list, 0, input_list.index(minv))
    elif mid_value > maxv:
        return swap_elements(input_list, 0, input_list.index(maxv))
    else:
        return swap_elements(input_list, 0, mid_index)


def swap_elements(input_list, first_index, second_index):
    swap = input_list[second_index]
    input_list[second_index] = input_list[first_index]
    input_list[first_index] = swap
    return input_list


def read_file(filename):
    file_contents = []
    with open(filename) as input_file:
        for line in input_file:
            file_contents.extend([int(x) for x in line.split()])
    return file_contents


quick_sort(read_file('3-QuickSort.txt'))
print(comparison_counter)
# 138382
