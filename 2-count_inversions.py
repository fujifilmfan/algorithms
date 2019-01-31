#!/usr/bin/env python


inversion_counter = 0


def count_inversions(input_list):
    results = []
    global inversion_counter
    if len(input_list) <= 1:
        # results.extend(list)
        # return results
        return input_list
    else:
        n = len(input_list)
        mid = len(input_list) // 2
        left = count_inversions(input_list[:mid])
        right = count_inversions(input_list[mid:])

        i = 0
        j = 0

        for _ in range(n):
            if i < len(left) and j < len(right):
                if left[i] < right[j]:
                    results.extend([left[i]])
                    i += 1
                else:
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
