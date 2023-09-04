

#use of nonlocal keyword
def show():
    name = "Sagar"
    def display():
        nonlocal name
        name = "Sham"
        print(name)
    display()
show()







import sys
sys.exit()


a=10
def show():
    global a
    print("global a=",a)
    a=20
    print("Modified a=",a)
show()


import sys
sys.exit()


a=10
def show():
    a=20
    print(a)
show()


import sys
sys.exit()

x=20 # global variable
def display():#local variable
    a=10
    b=20
    b+=10
    c=30
    print("value of x inside the function",x)
    print(a+b+c+x)

display()
print("value of x outside the function",x)






import sys
sys.exit()

def display():#local variable
    a=10
    b=20
    b+=10
    c=30
    print(a+b+c)

display()
