'''
Two number sum

Write a function that takes in a non-empty array of distinct integers and an 
integer representing a target sum. If any two numbers in the input array sum 
up to the target sum, the function should return them in an array, in any order.
If no two nums sum up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in
the array; you can't add a single integer to itself in order to obtain the target
sum.

You can assume that there will be at most one pair of numbers summing up to the
target sum.
'''


def two_number_sum(array, target_sum):
    # O(n^2)
    for n in range(len(array) - 1):
        first_number = array[n]
        for m in range(n + 1, len(array)):
            second_number = array[m]
            if first_number + second_number == target_sum:
                return [first_number, second_number]
    return []


def two_number_sum_hash(array, target_sum):
    # Time complexity O(n) n = lenght of input array
    # Space complecity O(n)
    hashtable = {}
    for number in array:
        eval_element = target_sum - number
        if eval_element in hashtable:
            return [eval_element, number]
        else:
            hashtable[number] = True
    return []


print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
