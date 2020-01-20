mylist = [1,2,3,4,5,6,7,8,9,10]

                                        # FOR LOOPS
for num in mylist:
    print(num)

for num in mylist:
    print('hello')

for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')

list_sum = 0
for num in mylist:
    list_sum += num

mystring = 'Hello World'
for letter in mystring:
    print(letter)

d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)

for item in d.items():
    print(item)

for key,value in d.items():
    print(value)

for value in d.values():
    print(value)

                                        # WHILE LOOPS  

x = 0
while x < 5: 
    print(f'The current value of x is {x}') 
    x++                                    