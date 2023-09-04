
def display():
    def message():
        return "How are you?"
    return message

fun = display()
print(fun())






import sys
sys.exit()

def display(str):
    def message():
        return "How are you?"
    result = message() + str
    return result

print(display(" Sagar"))








import sys
sys.exit()
def display(str):
    return "Hi" + str

x= display(" Sagar")
print(x)


import sys
sys.exit()
def calcuate_sum_list(lst):
    sum=0
    for item in lst:
        sum=sum+int(item)
    return sum

lst = [1,2,3,4,5,6,7,8,9,10]
result = calcuate_sum_list(lst)
print("The sum of all items in list=",result)







import sys
sys.exit()
def calculate(a,b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return sum,sub,mul,div

x= int(input("Enter the first value:"))
y= int(input("Enter the second value:"))
sum,sub,mul,div = calculate(x,y)
print("The sum of %d and %d = %d" %(x,y,sum))
print("The substraction of %d and %d = %d" %(x,y,sub))
print("The multiplication of %d and %d = %d" %(x,y,mul))
print("The division of %d and %d = %d" %(x,y,div))