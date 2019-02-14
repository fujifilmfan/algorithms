#!/usr/bin/env python


input_array_1 = [1, 5, 9, 3, 7, 2]
input_array_2 = [5, 3, 8, 9, 1, 7, 0, 2, 6, 4]


def merge_sort(input_list):
    results = []
    if len(input_list) <= 1:
        return input_list
    else:
        # Make recursive calls if a list has more than one element
        n = len(input_list)
        # Divide the list in half, rounding down ("//" is the floored division operator); an odd list will be divided
        # such that the left half if the smaller of the two, like this: [5, 3, 8, 9, 1] -> [5, 3] and [8, 9, 1]
        mid = len(input_list) // 2
        left = merge_sort(input_list[:mid])
        right = merge_sort(input_list[mid:])

        # Next, merge the two input lists stored in "left" and "right"
        # "i" and "j" keep track of the current index in "left" and "right", respectively
        i = 0
        j = 0

        for _ in range(n):
            # Add smaller of the next item in "left" and "right" to "results"; if "j" is longer than the length of
            # "right", then "right" has been exhausted and the elif statement is triggered if "i" is still less than
            # the length of "left"; if "i" is longer than "left", then "left" has been exhausted, and the else statement
            # is triggered.
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


# print(merge_sort(input_array_1))
merge_sort(input_array_2)
