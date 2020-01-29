def square(num):
    return num**2

myNum = [1,2,3,4,5]

for item in map(square,myNum):
    print(item)

list(map(square,myNum))

def splicer(st):
    if len(st)%2 == 0:
        return 'even'
    return st[0]

myNames = ['andy','sally', 'Mandy']
list(map(splicer,myNames))

def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]
list(filter(check_even,mynums))

# LAMBDA EXPRESSION
square = lambda number : number ** 2
square(5)
square(6)

list(map(lambda num : num**2,mynums))

check_even = lambda num : num%2 == 0
list(filter(lambda num : num%2 == 0,mynums))