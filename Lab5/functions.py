import random


def help_me():
    return help_description.encode('utf-8')


def hello(word):
    return word.encode('utf-8')


def is_prime(n):
    n = int(n)
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                ans = str(n) + " isn't a prime number!\n"
                ans = ans + str(i) + " * " + str(n // i) + " = " + str(n)
                break
            else:
                ans = str(n) + " is a prime number!\n"
    else:
        ans = str(n) + " isn't a prime number!\n"
    return ans.encode('utf-8')


def rect_area(x, y):
    ans = int(x) * int(y)
    return bytes(str(ans), 'utf-8')


def answer():
    return random.choice(yn).encode('utf-8')


def joke():
    return random.choice(jokelist).encode('utf-8')


help_description = \
    """
    ===============
    === h e l p ===
    ===============
    /help - displays this list of available commands
    
    /hello <text> - returns the text that was sent as param
    /prime <int> - tells if the given number is prime
    /area <int> <int> - tells the area of a rect with given x,y params
    
    /answer - responds to your most interested question with an 'yes' or 'no' 
    /joke - tells a python joke
    
    /exit - closes connection
    ===============
    """

yn = ['yes', 'no']

jokelist = \
    [
        'hey did you see that dat boi',
        'Someone:\"Do you know da wae?\"\nMe: \"Your memes make me want to die.\"',
        'On the eighth day god created memes',
        'meme?\n\n1 : an idea, belief or belief system, or pattern of behavior that spreads throughout a culture either vertically by cultural inheritance (as by parents to children) or horizontally by cultural acquisition (as by peers, information media, and entertainment media)\n\n2 : a pervasive thought or thought pattern that replicates itself via cultural means; a parasitic code, a virus of the mind especially contagious to children and the impressionable\n\n3 : the fundamental unit of information, analogous to the gene in emerging evolutionary theory of culture\n- meme pool (n.) : all memes of a culture or individual\n- memetic (adj.) : relating to memes\n- memetics (n.) : the study of memes\n\n4 : in blogspeak, an idea that is spread from blog to blog\n\n5 : an internet information generator, especially of random or contentless information ',
    ]
