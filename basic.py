# celcius to fahrenhrit
celcius = int(input("enter value"))
f = 1.8 * celcius + 32
print(f)



# reverse number
a = int(input("enter first number"))
b = int(input("enter second number"))
a , b = b , a
print(a,b)



 # sum of digits
a = int(input("enter the number"))
b = a % 10
c = (a // 10) % 10
d = (a //10) // 10
print(b+c+d)



 # without slicing

n = int(input("enter the four digit number"))
a = str(n % 10)
b = str((n // 10) % 10)
c = str(((n // 10) // 10) % 10)
d = str((((n // 10) // 10) // 10) % 10)
print(a+b+c+d)




 # with slicing(reverse the number)

n = (input("enter the four digit number"))
print(n[::-1])



 # even odd numbers
n = int(input("enter the number"))
if n%2 == 0:
    print("even")
else:
    print("odd")


 #leap year
n = int(input("enter the number"))
if n%400==0:
    print("leap year")
elif n%100==0:
    print("not leap year")
elif n%4==0:
    print("leap year")
else:
    print("not leap year")




 # distance between two points
a= int(input("enter first coordinate"))
b = int(input("enter second coordinate"))
x = int(input("enter third coordinate"))
y = int(input("enter fourth coordinate"))
d= ((x-a)*2+(y-b)2)*0.5
print(d)




# traiangle decleration
a = int(input("enter 1st angle"))
b = int(input("enter 2nd angle"))
c = int(input("enter 3rd angle"))
d = a+b+c
if d==180:
    print("triangle")
else:
    print("not a triangle")




 # declare profit and loss
cost = int(input("enter the cost amount"))
selling = int(input("enter the selling amount"))
if selling-cost>=0:
    print("profit")
else:
    print("loss")



#volume of cylinder and cost of milk
r = int(input("enter the radius of cylinder"))
h = int(input("enter the height of cylinder"))
a = int(input("enter the quantity of milk in liter"))
cost = a*40
v = 3.14*r**2*h
print(cost,v)




n = int(input("enter the number"))
if n%6==0 & n%3==0:
    print("divisible by 3 and 6")
else:
    print("not divisible")




# determine weather by temperature and humidity
t = int(input("enter the temperature"))
h = int(input("enter the value of humidity"))
if t>=30 and h>=90:
    print("hot an humid")
elif t>=30 and h<90:
    print("hot")
elif t<30 and h>=90:
    print("cool and humid")
else:
    print("cold")
