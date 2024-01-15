def find_outlier(integers):
    evenCount = 0
    oddCount = 0

    lastEvenIndex = -1
    lastOddIndex = -1

    for i, number in enumerate(integers):

        if number % 2 == 0:
            evenCount += 1
            lastEvenIndex = i
        elif number % 2 == 1:
            oddCount += 1
            lastOddIndex = i
    
    if evenCount < oddCount:
        return integers[lastEvenIndex]
    elif oddCount < evenCount:
        return integers[lastOddIndex]

# You are given an array (which will have a length of at least 3,
# but could be very large) containing integers.
# The array is either entirely comprised of odd integers or
# entirely comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and
# returns this "outlier" N.

# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)