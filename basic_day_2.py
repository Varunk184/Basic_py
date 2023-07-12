a = int(input())
b =int(input())
c = a*b
print(c)

###########################################################################################

a = int(input())
b = (a*1.8)+32
print(b)


###########################################################################################
a = int(input())

if a>0:
    print("Positive")
elif a==0:
    print("Zero")
else:
    print("Negative")
    


###########################################################################################


a = int(input())
if a%2 == 0:
    print("Even")
else:
    print("Odd")
    


##############################################################################################



a = int(input())
if a%4==0 and a%100!=0:
    print("Leap year")
elif a%400==0 and a%100==0:
    print("Leap year")
else:
    print("Is not a laep year")
    
    


#############################################################################################


a = int(input())
b =int(input())
c = int(input())

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
    
##############################################################################################

num = int(input())
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")