import numpy
import pandas
import math
import random

"""
def primes(N):
    X = []
    s = list(range(N+1))
    s[1] = 0
    position = 2
    while position <= N:
        if s[position] == position:
            X += [position]
            for i in list(range(2*position,N+1,position)):
                s[i] = 0
        position += 1
    return X

print(primes(100))
print(len(primes(10**6)))


p = round(random.random(), 2)
N = 100000
A = 0
B = 0

def deuce():
    score = 0
    while score < 2 and score > -2:
        r = random.random()
        if r < p: score = score + 1
        else: score = score - 1
    return score

for i in range(N):
    if deuce() > 0: A = A + 1
    else: B = B + 1

print(p, round(float(A)/float(N), 4), round((p**2)/(2*p*(p-1)+1), 4))
"""


class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Jonny')
p.say_hi()

name  = "Jonny"
def say_hi():
    print('Hello, my name is', self.name)
