#created on 20/09/2019
#author:samuvel
a=1
b=int(input('enter the ending number'))#getting the ending number
for i in range (a ,b+1):#using for loop to get values 
    if i%3==0 and i%5==0:# finding 0dd numbers
        print("FizzBuzz")
    elif (i%5==0):
        print("Buzz")
    elif (i%3==0):
        print("fizz")
    else:
        print(i)#entering other numbers
        
