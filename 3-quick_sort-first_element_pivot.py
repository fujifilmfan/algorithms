#!/usr/bin/env python


"""
Download the following text file:
QuickSort.txt

The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. The
integer in the ith row of the file gives you the ith entry of an input array.

Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. As you know,
the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different
pivoting rules.

You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length m,
you should simply add m-1 to your running total of comparisons. (This is because the pivot element is compared to each
of the other m-1 elements in the subarray in this recursive call.)

WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can
give you differing numbers of comparisons. For this problem, you should implement the Partition subroutine exactly
as it is described in the video lectures (otherwise you might get the wrong answer).

DIRECTIONS FOR THIS PROBLEM:

For the first part of the programming assignment, you should always use the first element of the array as the pivot
element.
"""


unsorted_list = [3, 8, 2, 5, 1, 4, 7, 6]


comparison_counter = 0


def quick_sort(input_list):
    # maybe there's a better way to implement a counter than using a global
    global comparison_counter
    # Implement recursion base case
    if len(input_list) <= 1:
        return input_list
    else:
        # the number of comparisons that will need to be done equals the length of the list - 1 (since one element
        # is the pivot)
        comparison_counter += len(input_list) - 1
        # Choose first element as pivot
        pivot = input_list[0]
        i = 1
        j = 1
        for _ in range(len(input_list)-1):
            # Increment "j" if it is already greater than (to the right of) the pivot
            if input_list[j] > pivot:
                j += 1
            # Swap "j" with the pivot if it is less than the pivot; increment both "i" and "j"
            else:
                swap = input_list[i]
                input_list[i] = input_list[j]
                input_list[j] = swap
                i += 1
                j += 1
        # Swap the pivot into it's proper position in the list
        swap = input_list[i-1]
        input_list[i-1] = input_list[0]
        input_list[0] = swap
        # Call quick_sort recursively with the left and right halves of the list
        left = quick_sort(input_list[:i-1])
        right = quick_sort(input_list[i:])
        # Join the left half, pivot, and right half of the list into one list
        input_list = left + [swap] + right
        return input_list


def read_file(filename):
    file_contents = []
    with open(filename) as input_file:
        for line in input_file:
            file_contents.extend([int(x) for x in line.split()])
    return file_contents


quick_sort(read_file('3-QuickSort.txt'))
print(comparison_counter)
# 162085
