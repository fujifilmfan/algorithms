#!/usr/bin/env python


def merge_sort(input_list):
    results = []
    if len(input_list) <= 1:
        return input_list
    else:
        n = len(input_list)
        mid = len(input_list) // 2
        left = merge_sort(input_list[:mid])
        right = merge_sort(input_list[mid:])

        i = 0
        j = 0

        for _ in range(n):

            if i < len(left) and j < len(right):
                if left[i] < right[j]:
                    results.extend([left[i]])
                    i += 1
                else:
                    results.extend([right[j]])
                    j += 1
            elif i < len(left):
                results.extend([left[i]])
                i += 1
            else:
                results.extend([right[j]])
                j += 1

    return results


print(merge_sort([1, 5, 9, 3, 7, 2]))
