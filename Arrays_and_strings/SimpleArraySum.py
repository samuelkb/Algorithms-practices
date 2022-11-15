"""
Problem description:
Given an array of integers, find the sum of its elements.

Complete the simpleArraySum function below.
"""


def simple_array_sum(array):
    """Receives an array and returns a sum of its values as int."""
    array_sum = 0
    for i in range(len(array)):
        array_sum += array[i]
    return array_sum


###########
#   Test  #
###########

simple_array = [1, 2, 3, 4, 10, 11]
result = simple_array_sum(simple_array)
print(result)
