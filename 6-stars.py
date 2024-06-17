def ch1():
    for i in range(1,5): 
        print("*")
#ch1()

#-----------------------------------------------------

def ch2():
    for i in range(1,5):
        print("*", end=" ")
#ch2()

#-----------------------------------------------------

def ch3():
    for i in range(1,5):
        for j in range(1,5):
            print("*", end=" ")
        print()
#ch3()

#-----------------------------------------------------

def ch4():
    for i in range(1,6):
        for j in range(1,i):
            print("*", end=" ")
        print()
#ch4()

#-----------------------------------------------------

def ch5():
    num=int(input("enter a number: "))
    for i in range(num):
        for j in range(i):
            print("*", end=" ")
        print()
#ch5()

#------------------------------------------------------

def ch6():
    num=int(input("enter a number: "))
    for i in range(num):
        for j in range(num):
            print("*", end=" ")
        print()
        num-=1
#ch6()

#--------------------------------------------------------

def ch7():
    num = int(input("Enter a number: "))
    for i in range(num):
        for k in range(num - i):
            print(" ", end=".")
        for j in range(i):
            print("*", end=" ")
        print()
#ch7()

#---------------------------------------------------------

def ch8():
    num = int(input("Enter a number: "))
    for i in range(num,0,-1):
        for j in range(num-i):
            print(" ",end=" ")
        for k in range(i):
            print("*", end=" ")
        print()
#ch8()

#----------------------------------------------------------

def ch9():
    num = int(input("num: "))
    
    for i in range(1, num + 1):
        spaces = " " * (num - i)
        stars = "*" * (2 * i - 1)
        print(spaces, stars)
    
    for i in range(num - 1, 0, -1):
        spaces = " " * (num - i)
        stars = "*" * (2 * i - 1)
        print(spaces,stars)

#ch9()

#----------------------------------------------------------

def ch10():
    num = int(input("num: "))

    for i in range(1, num):
        for j in range(1, i):
            print("*", end=" ")
        for k in range(2 * (num - i)):
            print(" ", end=" ")
        for l in range(1, i):
            print("*", end=" ")
        print()

    for i in range(num, 0, -1):
        for j in range(1, i):
            print("*", end=" ")
        for k in range(2 * (num - i)):
            print(" ", end=" ")
        for l in range(1, i):
            print("*", end=" ")
        print()

ch10()



