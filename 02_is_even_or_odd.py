def is_even_or_odd(number):
    #Uses the modulo operator to check the remainder of dividing the number by 2 and prints the result
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")


#Example function calls with both odd and even numbers
is_even_or_odd(31)
is_even_or_odd(10000020)