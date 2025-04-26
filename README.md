
# Name: Kamwaro Jesse Kariuki
AdmNo: 189730
---

# 1 Sum all elements in a list
The simple function takes in a list(array) as its parameter and iterates through it adding the elements together


+ Function definition
``` python
1. def summation(array):
    #initialises a variable sum
```
+  Initialises a variable sum
``` python
2.    sum = 0
```
+ Iterating through the list starting from the first element, adding each to sum
 ``` python
3.    for i in array:
4.        sum+=i
```
+ Returning the sum of all the elements
``` python
5.   return sum
```

+ Calling the function with an example list as the argument and printing the result
``` python
print(summation([1,2,3,4,5]))#Outputs 15
print(summation([]))#Outputs 0
print(summation([1,2,3,4,5,6,7]))#Outputs 28
```
# 2 Even or Odd
Uses the modulo operator to check the remainder of dividing the number by 2 and prints the result

+ Function definition
``` python
1. def is_even_or_odd(number):
```
+ Condition to check whether the remainder of division by 2 is 0 or 1 and prints accordingly
```python
2.   if number % 2 == 0:
3.        print(f"{number} is an even number")
```
+ Printing the result if odd
```python
4.    else:
5.        print(f"{number} is an odd number")
```



+ Example function calls with both odd and even numbers
```python
is_even_or_odd(31) #Outputs odd
is_even_or_odd(-3) #Outputs odd
is_even_or_odd(10000020) #Outputs even
```

# 3 Factorial
Multiplies each decremental number from an argument n up to 1 in a loop then returns the factorial which is then output to the console

+ Function definition
```python
def factorial(n):
```

+ Initialising a variable fact that will be multiplied within each loop iteration by n
```python
fact=1
```
+ If statement ensures no negatives can be passed during function calls
```python
if n<0:
        return "Error! No such factorial"
```
    
 
        
+ Multiply each decremental number from n up to 1(which is the lat number in the iterations greater than 0) then returns the factorial with the condition that as long as n is greater than 0
```python
  while n>0:
        fact = fact*n
        n = n-1
    return fact
```
+ Example of using the function
```python
print(factorial(4)) #Outputs 24
print(factorial(3)) #Outputs 6
```



# 4 Reverse a String

The function works by passing in a word, which is then converted to a list 
Another list, reversed_word is them initialised with 'none' values and then populated with the elements of the list of word.
The reversed_word elements are then joined together using the join() method

+ Function definition which takes in a string word, that is to be reversed
``` python
def reverse(word):
```
+ I converted word to a list of its letters assigning the list to a variable word_list
``` python
    word_list = list(word)
```
+ I initialised a list that is empty. I had initially assumed that assigning reversed_word to word_list creates a copy of word_list but it actually points to the same reference as word_list. So any further manipulation of reversed_word alters word_list as well leading to undesired results. So the better option was initialising an empty list, reversed_word with the length equal to word_list

    ``` python
    reversed_word = [None]*len(word)
    ```
+ After creating a variable equal to the length of the word, I iterate through the word, assigning every i-th element of reversed_word equal to every element of word_list from the last value. Because of zero indexing, we have to subtract 1 from length-i. This effectively reveses the string
    ``` python
    length = len(word)

    #Iterating through the length of the word and assigning every subsequent element of the empty list to every element from the last backwards
    for i in range(length):
        reversed_word[i] = word_list[length - i -1]
  ```
+ Using the join() function, the characters from the list reversed_word are joined to form one reversed string
   ``` python 
    #Joining every element of the reversed word to form one string
    print(''.join(reversed_word))
    ```

+ Example function calls with words and their reverses to see if they are the same
``` python
reverse("while")#Outputs 'elihw'
reverse("elihw")#Outputs 'while'

#Palindrome being the same forward and backwards
reverse("racecar")#Outputs 'racecar'

reverse("reverse")#Outputs 'esrever'
reverse("esrever")#Outputs 'reverse'
```
# 5 Factorial(with recursion)


+ Function definition
```python
def factorial(n):
```

+ Condition to ensure no negatives
```python
if n<0:
        return "Error! No such factorial"
```
    
+ Base case that makes sure there is a condition that terminates the recursive calls
+ As we continue multiplying n by the factorial of n-1, it will get to a point where 1 will be the return value then subsequent 'n's' get multiplied
```python

if n==0 or n==1:
        return 1

    return n*factorial(n-1)

```
    

+ Example calls of the factorial function with the same outputs of the previous factorial fuction
```python
print(factorial(-9)) #Outputs 'Error! No such factorial'
print(factorial(5)) #Outputs 120
print(factorial(6)) #Outputs 720
```

# 6 Sum of digits in a number
Since the number passed into the function is in base-10, then the remainder after dividing the number by 10 is the last digit of the number
Using a loop can help where with each iteration, we floor divide n by 10 to get the new n


Modulus operator is used to give the remainder of the number
+ Function definition
```python
def sum_digits(n):
```


+ Initialises a variable sum that will be used to add the individual digits
```python
sum = 0
```
    
+ Condition to return 0 if 0 is the argument
```python
if n == 0:
        return 0
```
    
+ Loop with the condition being as long as n > 0 which terminates when the condition is false
```python
while n > 0:
```
    
+ Assigns sum to the previous value and adds it to the remainder after division with 10
+ Division by 10 gives an individual digit for any decimal number 
```python
sum = sum + n%10
```
        

+ Floor division is used to get the new integer n that ensures we always remove the remainder with every loop iteration
```python
 n = n//10
```
       
+ The function returns the sum of all the digits in the number
```python
return sum
```
    
+ Example function calls
```python
print(sum_digits(56)) #Outputs 11
print(sum_digits(104)) #Outputs 5
```

