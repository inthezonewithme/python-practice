def sum_digits(n):

    #Initialises a variable sum that will be used to add the individual digits
    sum = 0

    if n == 0:
        return 0

    while n > 0:
        #assigns sum to the previous value and adds it to the remainder after division with 10
        #division by 10 gives an individual digit for any decimal number
        sum = sum + n%10

        #floor division is used to get the new integer n that ensures we always "remove" the remainder with every loop iteration
        n = n//10

    return sum

print(sum_digits(56))
print(sum_digits(104))