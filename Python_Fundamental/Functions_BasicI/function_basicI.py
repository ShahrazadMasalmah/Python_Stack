#1
def a():
    return 5
print(a()) # The output is 5

#2
def a():
    return 5
print(a() + a()) #The output is 10 (a()=>5 then 5 + 5 => 10)

#3
def a():
   return 5
   return 10
#print(a()) # The output is 5 because in function when we encouter the return 
#this means the end of calling the function

#4
def a():
    return 5
    print(10)
print(a()) # The output is 5 for the same reason in #3

#5
def a():
    print(5)
x = a()
print(x)    #The output is 5 and none , 5 for when we called the function it printed the print inside of it
# and none for the print (x) because there is a return variable from the function

#6
def a(b,c):
   print(b+c)
print(a(1,2) + a(2,3)) #The output is 3, 5, and TypeError because it runs 
#the function and print the sum of 1 and 2 => 3, and this goes for 2 and 3 => 5
#The error for printing the sum of the 2 functions it said 
#TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5)) # The output is 25 string because it conveted the two number to string

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a()) # The output is 100 from print(b) and 10 from else statement because b > 10

#9
def a(b,c):
    if b < c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) # The output is 7 because 2 < 3
print(a(5,3)) # The output is 14 because 5 > 3
print(a(2,3) + a(5,3)) # The output is 21 because the sum of a(2,3)=>7 + a(5,3)=>14

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5)) # The output is 8 from return b + c

#11
b = 500
print(b) 
def a():
    b = 300
    print(b)
print(b)
a()
print(b) 
# The output of the first print is 500, the second one is 500, and then calling the function
#print 300, the last one is 500 so the output (500 500 300 500)

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# The output of the first print is 500, the second one is 500, and then calling the function
#print 300 and change the value of b to 300 by the return from the function 
#the last one is 300 so the output (500 500 300 300)

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# The ouptut is 1 3 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# The output is 1 3 5 10 


 











