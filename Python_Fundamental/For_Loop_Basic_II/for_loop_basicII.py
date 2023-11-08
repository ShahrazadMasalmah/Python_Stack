#1.  Given a list, write a function that changes all positive numbers in the list to "big".
def biggie_size(list):
    for i in range(0,len(list)):
        if(list[i] > 0):
            list[i] = "big"
    return list
print(biggie_size([-1, 3, 5, -5])) 

#2. Given a list of numbers, create a function to replace the last value with the number of positive values. 
def count_positives(list):
    count = 0
    for i in range(0, len(list)):
        if list[i] > 0:
            count += 1
    list[len(list) - 1] = count
    return list
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

#3. Create a function that takes a list and returns the sum of all the values in the list.
def sum_total(list):
    sum = 0
    for value in list:
        sum += value
    return sum
print(sum_total([1,2,3,4])) 
print(sum_total([6,3,-2]))

#4. Create a function that takes a list and returns the average of all the values.
def average(list):
    sum = 0
    for value in list:
        sum += value

    avg = sum / len(list)
    return avg
print(average([1,2,3,4]))

#5. Create a function that takes a list and returns the length of the list.
def length(list):
    count = 0
    for i in list:
        count += 1

    return count
print(length([37,2,1,-9]))
print(length([]))

#6. Create a function that takes a list of numbers and returns the minimum value in the list.
def minimum(list):
    if len(list) == 0:
        return False
    
    min = list[0]
    for i in range(1, len(list)):
        if min > list[i]:
            min = list[i]
    return min
print(minimum([37,2,1,-9])) 
print(minimum([])) 

#7. Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
def maximum(list):
    if len(list) == 0:
        return False
    
    max = list[0]
    for i in range(1, len(list)):
        if max < list[i]:
            max = list[i]
    return max
print(maximum([37,2,1,-9])) 
print(maximum([])) 

#8. Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis(list):
    dict = {}  
    sum = 0  
    min = list[0]
    for i in range(0, len(list)):
        sum += list[i]
        if min > list[i]:
            min = list[i]
        else:
            max = list[i]
    avg = sum/len(list)
    dict['sumTotal'] = sum
    dict['average'] = avg
    dict['minimum'] = min
    dict['maximum'] = max
    dict['length'] = len(list)

    return dict
print(ultimate_analysis([37,2,1,-9]))

#9. Create a function that takes a list and return that list with values reversed.
def reverse_list(list):
    i = 0
    j = len(list)-1
    while j > i:
        list[i], list[j] = list[j], list[i]
        i += 1
        j -= 1

    return list
print(reverse_list([1,50,3,-4,100]))    




