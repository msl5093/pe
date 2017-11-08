def getMultiplesOf(x, y, nums):
    listOfNums = xrange(nums)
    multiples = [n for n in listOfNums if n % x == 0 or n % y == 0]
    return sum(multiples)

print(getMultiplesOf(3, 5, 1000))