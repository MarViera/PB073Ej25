import random

print(random.getrandbits(8))
print(random.randrange(0,100))
print(random.randint(0,100))
input()
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
print(random.choice(SYMBOLS))
chares = []
for i in range (33,47,1):
    chares += chr(i)
for i in range (58,64,1):
    chares += chr(i)
for i in range (91,96,1):
    chares += chr(i)
for i in range (123,126,1):
    chares += chr(i)
print(chares)
input()
print(random.choice(chares))
print(random.random())
print(random.uniform(0,100))
sym = list(SYMBOLS)
random.shuffle(sym)
print(sym)
print(random.sample(SYMBOLS,5))

