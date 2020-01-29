for num in range(2,20,3):
    print(num)

x = list(range(2,20,3))

index_Count = 0
word = 'abcde'
for letter in word:
    print('At index {} the letter is {}'.format(index_Count,letter))
    index_Count += 1

index_Count = 0
word = 'abcde'
for letter in word:
    print(word[index_Count])
    index_Count += 1

word = 'i am caio'
for item in enumerate(word):
    print(item)

for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

myList1 = [1,2,3,4,5]
myList2 = ['a','b','c','x']

for item in zip(myList1,myList2):
    print(item)

'x' in myList1
'x' in myList2

d = {'myKey': 345}
'myKey' in d

345 in d.values()

score = [10,20,30,40,100]
min(score)
max(score)

from random import shuffle
scores = [1,2,3,4,5,6,7,8,9,10]
shuffle(scores)
scores

from random import randint
randint(0,100)
x = randint(0,100)
x

name = input('What is your name: ')
age = int(input('Enter your age here: '))

## COMPREHENSION LISTS 

hello = 'hello caio'
myString = [letter for letter in hello]
myString

values = [num**2 for num in range(0,11)]
values

values = [num**2 for num in range(0,11) if num%2 == 0]
values

celcius = [0,10,20,30.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
fahrenheit

#               EXERCICIOS

st = 'Print only the words that start with s in this sentence'
for word in st.split(' '):
    if word.startswith('s'):
        print(word)

result = [num for num in range(1,51) if num%3 == 0]
result

for word in st.split(' '):
    if len(list(word)) % 2 == 0:
        print(word)

