def findMinSum(num):
    sum = 0
    i = 2
    while (i * i <= num):
        while (num % i == 0):
            sum += i
            num /= i
        i += 1
    sum += num

    # Return sum of numbers
    # having minimum product
    return sum
#########################################################################

# Driver Code
num = 12
a  = findMinSum(num)
print(a)
