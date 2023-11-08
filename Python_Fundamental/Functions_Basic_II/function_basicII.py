#1. Create a function that accepts a number as an input. Return a new list that counts down by one, from the number
def countdown(num):
    list=[]
    for i in range(num, -1, -1):
        list.append(i)
    return list
print(countdown(5))

#2. Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2])) 
 
#3. Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_plus_length(list):
    sum = list[0] + len(list)
    return sum  
print(first_plus_length([1,2,3,4,5])) 

#4. Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value.
def values_greater_than_second(list):
    newList=[]
    for i in range(0,len(list)):
        if len(list) >=2: 
           if list[i] > list[1]:
               newList.append(list[i])
        else:
            return False
    return newList
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3])) 

#5. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def length_and_value(size,value):
    list=[]
    for size in range(size, 0, -1):
        list.append(value)
    return list
print(length_and_value(4,7))
print(length_and_value(6,2))           