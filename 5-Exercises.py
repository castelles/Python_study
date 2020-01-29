def lesser_of_two_events(x,y):
    if x%2 == 0 and y%2 == 0:
        return min(x,y)
    else:
        return max(x,y)

result = lesser_of_two_events(2,4)

def animalCrackers(text):
    words = text.split(' ')
    return words[0][0].lower == words[1][0].lower

animalCrackers('Carro Caio')

def makesTwenty(x,y):
    return x == 20 or y == 20 or x+y == 20

makesTwenty(15,5)

def old_macdonald(text):
    if len(text) > 3:
        return text[:3].capitalize() + text[3:].capitalize()

old_macdonald('macdonald')

def masterYoda(text):
    words = text.split()
    return ' '.join(words[::-1])

masterYoda('I am home')

def almostThere(num):
    return (abs(100 - num) <= 10 or abs(200 - num) <= 10)

def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i,i+1]==[3,3]:
            return True
    return False

test = 'hi'

def paperDoll(text):
    result = ''
    for letter in text:
        result += letter*3
    return result

paperDoll('hello')

def blackjack(x,y,z):
    if sum(x,y,z) <= 21:
        return sum(x,y,z)
    if sum(x,y,z) <= 31 and 21 in (x,y,z):
        return sum(x,y,z)-10
    else:
        return 'BUST'

blackjack(10,12,11)

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

summer_69([4, 5, 6, 7, 8, 9])

def spyGame(arr):
    code = [0,0,7,'x']
    for num in arr:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

spyGame([1,2,3,4,0,0,7])

def count_Primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

count_Primes(54)
