def factorial(n):
    fact=1

    #multiply each decremental number from n up to 1 then returns the factorial
    if n<=0:
        return "Error! No such factorial"
    while n>0:
        fact = fact*n
        n = n-1
    return fact

#example of using the function
print(factorial(4))
print(factorial(3))

