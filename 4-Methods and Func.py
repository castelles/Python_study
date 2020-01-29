# Documentation
def novaFunc():
    '''
    First function of a new programmer\n
    Prints 'Hello World' string
    '''
    print('Hello World!')

def say_Hello_To(name='NAME'):
    print('Hello '+name)

say_Hello_To('Caio')
say_Hello_To()

def say_Hello_To(name='NAME'):
    return 'hello ' + name

saying = say_Hello_To('Caio')
saying

def dog_Check(stringWithDog):
    return 'dog' in stringWithDog.lower()

dog_Check('Dog ran away')

def pig_Latin(word):
    '''
    Transform any word into a encripted new word\n
    If a word start with a vowel, add 'ay' to its end\n
    If does not start with a vowel, put the first letter
    to the end, than add 'ay'
    '''
    firstLetter = word[0]
    
    if firstLetter in 'aeiou':
        pigWord = word + 'ay'
    else:
        pigWord = word[1:] + firstLetter + 'ay'
    
    return pigWord

pig_Latin('word')