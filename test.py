# print those number which is equal to sum of its digits square
n = int(input("enter the 3 digit number"))
a = n%10
b = (n//10)%10
c = (n//10)//10
d = a*2+b2+c*2
print(d)



# armstrong number
n = int(input("enter the 3 digit number"))
a = n%10
b = (n//10)%10
c = (n//10)//10
d = a*3+b3+c*3
if n==d:
    print("armstrong number")
else:
    print("not a armstrong number")



# narcissist number
n = int(input("enter the four digit number"))
a = n%10
b = (n//10)%10
c = ((n//10)//10)%10
d = ((n//10)//10)//10
e = a*4+b4+c4+d*4
if n==e:
    print("narcissist number")
else:
    print("not narcissist number")




# in hand salary after reducing hra,da,pf,tax
salary = int(input("enter the salary in lpa"))
hra = salary*0.1
da = salary*0.05
pf = salary*0.03
if 5<=salary<10:
    inhand_salary = salary-hra-da-pf-salary*0.1
    print("current salary:",inhand_salary)
elif 11<=salary<20:
    inhand_salary = salary-hra-da-pf-salary*0.2
    print("current salary:",inhand_salary)
else:
    inhand_salary = salary-hra-da-pf-salary*0.3
    print("current salary:",inhand_salary)



# menu driven program
user_input = int(input('''hii welcome to our program.
what you would like to do!
1.cm to ft
2.kl to miles
3.usd to inr
4.exit'''))
if user_input==1:
    cm = int(input("enter the value which you want to convert"))
    ft = cm*0.0328084
    print(ft,"ft")
elif user_input==2:
    kl = int(input("enter the value which you want to convert"))
    miles = kl*0.621371
    print(miles,"miles")
elif user_input==3:
    usd = int(input("enter the value which you want to convert"))
    inr = usd*94.51
    print(inr,"inr")
else:
    print("exit")




# finding no. of dogs and chickens
h = int(input("enter the number of heads:"))
l = int(input("enter the number of legs:"))

y = (4*h-l)*0.5
x = (l-2*h)*0.5
print("dogs:",x)
print("chicken:",y)




# reverse the number
num = int(input("enter the number"))
print(str(num)[::-1])



# sum of 1 to n
n = int(input("enter the number"))
sum = 0
for i in range(n+1):
    
    sum = sum+i
print(sum)





# multiply two numbers without using multiple operator
a = int(input("enter the first number"))
b = int(input("enter the second number"))
result = 0
for i in range(b):
    result = result+a
print(result)




# factorial
n = int(input("enter the number"))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print(fact)






# odd numbers 1 to 25
n = int(input("enter the number"))
for i in range(1,n+1):
    if i%2==0:
        print( )
    else:
        print(i)





# check the number is prime or not!

n = int(input("enter the number"))
if n == 2:
    print("prime")
elif n>1:
    
    for i in range(2,n):
        if (n % i)==0:
            print("not a prime")
            break
        else:
            print("prime number")
            break
else:
    print("not a prime")





# find three digit armstrong number
for i in range(100,1000):
    a = i%10
    b = (i//10)%10
    c = (i//10)//10
    d = a*3+b3+c*3
    if i == d:
        print(i)






# populations previous 10 years serialwise
population = 10000
for i in range(10 ,0 ,-1):
    population = population*0.9
    print(population)







#unique combinations of 1,2,3,4
for i in range(1,5):
     for j in range(1,5):
         if (i!=j):
             print(i,j)





# hcf of two numbers
n1 = int(input("enter the first no:"))
n2 = int(input("enter the second no:"))
if n1 < n2:
    n1 ,n2 = n2 ,n1
while (n2!=0):
    rem = n1%n2
    n1 = n2
    n2 = rem
hcf = n1
print("hcf is",n1)








# lcm of two numbers 
a = int(input("enter the first no:"))
b = int(input("enter the second no:"))

n1 = a
n2 = b
if n1 < n2:
    n1 ,n2 = n2 ,n1
while (n2!=0):
    rem = n1%n2
    n1 = n2
    n2 = rem
hcf = n1
lcm = (a*b)//hcf
print(lcm)






# first 20 numbers of fibonacci sequence
a = 0
b = 1
sum = 0
for i in range(20):
    sum = a+b
    a = b
    b = sum
    print(sum)




#compound intrset
p = int(input("enter the principle amount"))
r = float(input("enter rate of intrest"))
t = int(input("enter the time"))
a = p*(1+r/100)**t
compound_intrest = a - p
print(compound_intrest)







# compute value of n + nn + nnn
n = input("enter number")
result = int(n) + int(n+n) + int(n+n+n)
print(result)




# number of digits in any number
n = int(input("enter no.:"))
count = 0
while (n>0):
    n = n // 10
    
    count += 1
print(count)




#factors of any given number
n = int(input("enter no.:"))

for i in range(1,n+1):
    if n%i==0:
        result = i
        print(i)
