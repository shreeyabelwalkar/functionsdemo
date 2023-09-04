#keyword arguments
def display(farg, **kwargs):
    print("Formal argument=", farg)
    for x,y in kwargs.items():
        print("key={}, value={}".format(x,y))


display(101, eno=501, name="sagar")




import sys
sys.exit()
#variable length arguments)
def display(farg, *args):
    print(farg)
    print(*args)

    sum=farg
    for item in args:
        sum=sum+item
    print("sum=",sum)

display(11,22,33,44,55,66,77,88,99,109)

import sys
sys.exit()


#default arguments
def shop(item,price=42.22):
    print("Item=",item)
    print("price=", price)


shop(price= 23.56, item="Sugar")
shop(item="Oil")



import sys
sys.exit()
#keyword arguments
def shop(item,price):
    print("Item=",item)
    print("price=", price)

shop(item="Sugar", price= 56.23)
shop(price= 23.56, item="Sugar")


import sys
sys.exit()

#positional arguments
def display(a,b,c): #function definition
    print(a+b+c)

x= 10 #calling of function
y=20
z=20
display(x,y,z)