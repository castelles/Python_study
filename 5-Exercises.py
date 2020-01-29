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
    return x == 20 or y == 20 or x+y == 20:

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
    return false

test = 'hi'

def paperDoll(text):
    result = ''
    for letter in text:
        result += letter*3
    return result

paperDoll('hello')

def blackjack(x,y,z):
    if x+y+z <= 21:
        return x+y+z
    if x+y+z <= 31 and 21 in (x,y,z):
        return x+y+z-10
    else:
        return 'BUST'

blackjack(10,12,11)
