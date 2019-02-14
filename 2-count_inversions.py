#!/usr/bin/env python


"""
Download the following text file:
IntegerArray.txt

This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer
repeated.

Your task is to compute the number of inversions in the file given, where the ith row of the file indicates
the ith entry of an array.

Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the
video lectures.
"""


inversion_counter = 0


def count_inversions(input_list):
    # See "2-merge_sort.py" for additional code comments
    results = []
    global inversion_counter
    if len(input_list) <= 1:
        return input_list
    else:
        n = len(input_list)
        mid = len(input_list) // 2
        left = count_inversions(input_list[:mid])
        right = count_inversions(input_list[mid:])

        # Implement merge algorithm as in "2-merge_sort.py" with a counter added.
        i = 0
        j = 0

        for _ in range(n):
            if i < len(left) and j < len(right):
                if left[i] < right[j]:
                    results.extend([left[i]])
                    i += 1
                else:
                    # Count an inversion when left[i] > right[j]
                    results.extend([right[j]])
                    inversion_counter += len(left[i:])
                    j += 1
            elif i < len(left):
                results.extend([left[i]])
                i += 1
            else:
                results.extend([right[j]])
                j += 1
    return results


def read_file(filename):
    file_contents = []
    with open(filename) as input_file:
        for line in input_file:
            file_contents.extend([int(x) for x in line.split()])
    return file_contents


count_inversions(read_file('2-IntegerArray.txt'))
print(inversion_counter)
