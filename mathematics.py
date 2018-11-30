# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 12:46:37 2018

Work-in-progress program frameworks for mathematics functions based on https://www.khanacademy.org/math

@author: alanp
"""

import math

#insert number of items to be counted as input characters
def count(items):
    n = 0
    for i in items:
        n += 1
    print(str(n) + " items counted")

#add a and b
def addition(a, b):
    n = 0
    n = a + b
    print(str(a) + " + " + str(b) + " = " + str(n))

#subtract b from a, or subtract a by b
def subtraction(a, b):
    n = 0
    n = a - b
    print(str(a) + " - " + str(b) + " = " + str(n))

#identify place value of number
def placevalue(num, place):
    n = 0
    p = int(math.log(place, 10)) + 1
    s = str(num)
    n = s[len(s) - p]
    print('place value of ' + str(place) + ' in ' + str(num) + ' is ' + str(n))

#compare the size of a to b
def comparesize(a, b):
    if a == b:
        print('a = b')
    elif a > b:
        print('a > b')
    elif a < b:
        print(str(a) + ' < ' + str(b))

#consecutively order a string of numbers ascending
def ascend(num):
    ns = []
    for i in str(num):
        ns.append(i)
    ns.sort()
    n = ''
    for i in ns:
        n += str(i)
    print(n)

#consecutively order a string of numbers descending
def descend(num):
    ns = []
    for i in str(num):
        ns.append(i)
    ns.sort()
    nsi = []
    for i in reversed(ns):
        nsi.append(i)
    n = ''
    for i in nsi:
        n += str(i)
    print(n)
    
#identify shape by number of vertices num to a square
def identifyshape(vert):
    if vert == 1:
        print('this is a point')
    elif vert == 2:
        print('this is a line')
    elif vert == 3:
        print('this is a triangle')
    elif vert == 4:
        print('this is a square')

#addition with currency
def currencyadd(a, b):
    n = 0
    n = a + b
    n = str(n)
    if '.' not in n:
        n += '.00'
    else:
        if (len(n) - n.index('.')) < 3:
            n += '0'
    print(n)

#subtraction with currency
def currencysubtract(a, b):
    n = 0
    n = a - b
    n = str(n)
    if '.' not in n:
        n += '.00'
    else:
        if (len(n) - n.index('.')) < 3:
            n += '0'
    print(n)

#addition with time
def timeadd(t, a):
    hours = ''
    seconds = ''
    t = str(t)
    hr = t.index(':')
    hours = t[0 : hr]
    seconds = t[hr+1 : len(t)]
    a = str(a)
    hr = a.index(':')
    hours = int(hours) + int(a[0 : hr])
    seconds = int(seconds) + int(a[hr+1 : len(a)])
    if seconds > 59:
        hr = int(seconds / 60)
        hours += hr
        seconds = seconds - 60*hr
    hr = str(hr)
    seconds = str(seconds)
    if (len(seconds) < 2):
        seconds += '0'
    print(str(hours) + ':' + str(seconds))

#addition with angles
def angleadd(a, b):
    n = 0
    n = a + b
    n = n % 360
    print(str(a) + ' and ' + str(b) + ' degrees = ' + str(n) + ' degrees')

#subtraction with angles
def anglesubtract(a, b):
    n = 0
    n = a - b
    n = n % 360
    print(str(a) + ' and ' + str(b) + ' degrees = ' + str(n) + ' degrees')

#a times b
def multiply(a, b):
    n = 0
    n = a * b
    print(str(a) + ' * ' + str(b) + ' = ' + str(n))

#a divided by b
def divide(a, b):
    n = 0
    n = a / b
    print(str(a) + ' / ' + str(b) + ' = ' + str(n))

#remainder of a divided by 
def remainder(a, b):
    n = 0
    n = a % b
    print('remainder of ' + str(a) + ' / ' + str(b) + ' = ' + str(n))

#fraction, incomplete; only works with two digits
def fraction(a):
    if a <= 1:
        nume = 1
        deno = 1/a
        m = 2
        while (deno % 1) != 0:
            nume = nume / (m-1)
            deno = deno / (m-1)
            nume = nume * m
            deno = deno * m
            m += 1
    elif a > 1:
        nume = a
        deno = 1
        m = 2
        while (nume % 1) != 0:
            nume = nume / (m-1)
            deno = deno / (m-1)
            nume = nume * m
            deno = deno * m
            m += 1
    print(str(nume) + ' / ' + str(deno))

#incomplete add fraction
def addfraction(a, b):
    num = []
#incomplete subtract fraction
def subtractfraction(a, b):
    num = []

#measurements of triangle and square shapes
def perimetertriangle(l, w):
    p = l + w + math.sqrt(math.pow(l, 2) + math.pow(w, 2))
    print('triangle perimeter = ' + str(p))
def perimetersquare(l, w):
    p = 2*l + 2*w
    print('square perimeter = ' + str(p))
def perimetercircle(r):
    p = 2 * math.pi * r
    print('circle perimeter = ' + str(p))
def areatriangle(l, w):
    a = l * w / 2
    print('triangle area = ' + str(a))
def areasquare(l, w):
    a = l * w
    print('square area = ' + str(a))
def areacircle(r):
    p = math.pi * math.pow(r, 2)
    print('circle area = ' + str(p))
#incomplete geometry tools, consider moving to separate file


#finds the highest prime number up to num
def isprime(num):
    for i in range(2, num):
        if (num % i) == 0:
            print(str(num) + ' is not a prime number. (divisible by ' + str(i) + ')')
    print(str(num) + ' is a prime number')

#lists factors of a number
def factors(num):
    factors = []
    factors.append(num)
    for i in range(1, num):
        if (num % i) == 0:
            factors.append(i)
    print('factors of ' + str(num) + ' is ' + str(factors))

#incomplete lists prime factors of a number
def primefactors(num):
    factors = []

#incomplete solve for y = ax + b
def algebra(formula):
    formula = []

#returns a is % of b /round function glitches for some reason
def percentage(a, b):
    p = 0
    p = round(a / b, 2)
    p = p * 100
    print(str(a) + ' is ' + str(p) + '% of ' + str(b))
