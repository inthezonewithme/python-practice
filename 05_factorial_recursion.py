def factorial(n):

    if n<0:
        return "Error! No such factorial"
    #Base case that makes sure there is a condition that terminates the recursive calls
    #As we continue multiplying n by the factorial of n-1, it will get to a point where 1 will be the return value then subsequent 'n's' get multiplied
    if n==0 or n==1:
        return 1

    return n*factorial(n-1)

#Example calls of the factorial function with the same outputs of the previous factorial fuction
print(factorial(-9))
print(factorial(5))
print(factorial(6))