# problem - 1
n = int(input("enter no.:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()






# problem - 2
n = int(input("enter no.:"))
for i in range(1,n+1):
    if (i<=3):
        for j in range(1,i+1):
            print("*",end=" ")
    else:
        for j in range(1,n-i+2):
            print("*",end=" ")
    print()





# problem - 3
n = int(input("enter no.:"))
for i in range(1,n+1):
    for j in range(1,2*i):
        print("*", end=" ")
    print()



#problem - 4
n = int(input("enter no.:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    for j in range(i-1,0,-1):
        print(j, end=" ")
    print()




# problem - 5
n = int(input("enter number"))
count = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(count,end=" ")
        count += 1
    print()
