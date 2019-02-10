#!/usr/bin/env python

unsorted_list = [3, 8, 2, 5, 1, 4, 7, 6]


comparison_counter = 0


def quick_sort(input_list):
    global comparison_counter
    if len(input_list) <= 1:
        return input_list
    else:
        comparison_counter += len(input_list) - 1
        pivot = input_list[0]
        i = 1
        j = 1
        for _ in range(len(input_list)-1):
            if input_list[j] > pivot:
                j += 1
            else:
                swap = input_list[i]
                input_list[i] = input_list[j]
                input_list[j] = swap
                i += 1
                j += 1
        swap = input_list[i-1]
        input_list[i-1] = input_list[0]
        input_list[0] = swap
        left = quick_sort(input_list[:i-1])
        right = quick_sort(input_list[i:])
        input_list = left + [swap] + right
        return input_list

def read_file(filename):
    file_contents = []
    with open(filename) as input_file:
        for line in input_file:
            file_contents.extend([int(x) for x in line.split()])
    return file_contents


# print(quick_sort(read_file('3-QuickSort.txt')))
# print(quick_sort(unsorted_list))

quick_sort(read_file('3-QuickSort.txt'))
# quick_sort(unsorted_list)
print(comparison_counter)
# 162085