def reverse(word):
    #Creating a list of characters of the "word" argument to be passed
    word_list = list(word)

    #Initialising an empty list of 'none' values that is equal to the length of the word
    reversed_word = [None]*len(word)

    length = len(word)

    #Iterating through the length of the word and assigning every subsequent element of the empty list to every element from the last backwards
    for i in range(length):
        reversed_word[i] = word_list[length - i -1]
    #Joining every element of the reversed word to form one string
    print(''.join(reversed_word))


#Example function calls with
reverse("while")
reverse("elihw")

#Palindrome being the same forward and backwards
reverse("racecar")

reverse("reverse")
reverse("esrever")
