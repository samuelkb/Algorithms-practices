import unittest


def two_number_sum(array, target_sum):
    # O(n^2)
    for n in range(len(array) - 1):
        first_number = array[n]
        for m in range(n + 1, len(array)):
            second_number = array[m]
            if first_number + second_number == target_sum:
                return [first_number, second_number]
    return []


print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
