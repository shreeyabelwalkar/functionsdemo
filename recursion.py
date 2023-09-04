def factorial(num):
    if num == 0:
        result=1
    else:
        result = num*factorial(num-1)
    return result

for i in range(1,11):
    result=factorial(i)
    print("Factorial of {}={}".format(i,result))