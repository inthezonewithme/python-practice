def summation(array):
    sum = 0
    for i in array:
        sum+=i
    return sum

print(summation([1,2,3,4,5]))
print(summation([]))
print(summation([1,2,3,4,5,6,7]))