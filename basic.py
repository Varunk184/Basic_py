# This program prints Hello, world!
print('Hello, world!')

# This program adds two numbers
a = int(input())
b =int(input())
c = a+b
print(c)

# Squre root
a = int(input())
b = a**0.5
print(format(b,'0.2f'))

# Python Program to find the area of triangle

a = int(input())
b =int(input())
c = int(input())

s = (a + b + c) / 2


area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(format(area,'0.2f'))


# Solve the quadratic equation ax**2 + bx + c = 0

import cmath

a = int(input())
b =int(input())
c = int(input())

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print(sol1,sol2)

# Python program to swap two variables

x = int(input())
y = int(input())
temp = x
x = y
y = temp
print(x,y)

# Program to generate a random number between 0 and 9
import random
print(random.randint(0,9))



# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))


conv_fac = 0.621371

miles = kilometers * conv_fac
print(format(miles,'0.2f'))

# last basic code of the day

a = int(input())
b = int(input())
if a>b:
    print(a)
else:
    print(b)
