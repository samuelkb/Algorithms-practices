# Description:
# Given an array of integers, find the sum of its elements.

#
# Complete the simpleArraySum function below.
#


def simpleArraySum(ar):
    """Recieves an array and returns a sum of its values as int."""
    arraySum = 0
    for i in range(len(ar)):
        arraySum += ar[i]
    return arraySum


###########
#   Test  #
###########

simpleArray = [1, 2, 3, 4, 10, 11]
result = simpleArraySum(simpleArray)
print(result)
