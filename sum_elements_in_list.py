def summation(array):
    #initialise a variable sum
    sum = 0

    #iterate through the list starting from the first element, adding each to sum
    for i in array:
        sum+=i
    return sum


#calling the function with an example list as the argument and printing the result
print(summation((1,2,3,4,5)))
