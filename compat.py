from random import randint

xrange = range
file = open

def randomChar(self, y):
    return ''.join(random.choice(ascii_letters) for x in range(y))
