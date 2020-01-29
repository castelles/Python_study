def ran_check(num,low,high):
    return num > low and num< high

ran_check(10,1,12)

def up_low():
    s = input('Escreva algo: ')
    upper = 0
    lower = 0
    for letter in s:
        if letter.islower():
            lower += 1
            continue
        if letter.isupper():
            upper += 1
    print(f'No. of Upper case characters: {upper}\nNo. of Lower case characters: {lower}')

up_low()

def uniqueList(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

uniqueList([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4])

def multiply(lst):
    result = 1
    for num in lst:
        result *= num
    return result

multiply([1,2,3,-4])

def palindrome(text):
    return text == text[::-1]

palindrome('hellehn')

import string
def ispangram(text):
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        if letter not in text:
            return False
    return True

ispangram("The quick brown fox jumps over the lazy dog")
