"""
Problem description:
In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that
some of those integers may be quite large.

Function Description
Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.
aVeryBigSum has the following parameter(s):
    int ar[n]: an array of integers .
Return
    long: the sum of all array elements
"""


def aVeryBigSum(ar):
    big_sum = 0
    for i in range(len(ar)):
        big_sum += ar[i]
    return big_sum


###########
#   Test  #
###########

ar_count = int(5)
ar = list(map(int, ([1000000001, 1000000002, 1000000003,
                     1000000004, 1000000005])))
result = aVeryBigSum(ar)
print(result)
