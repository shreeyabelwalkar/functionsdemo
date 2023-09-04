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