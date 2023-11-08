# Insertion Sort
arr_list = [6,5,3,1,8,7,2,4]
arr_list2 = [2,4,100,-1,-50,11,-9]

def insertionSort(arr_list):
    for i in range(len(arr_list) - 1):
        #print("I am i",i)
        for j in range(i,-1, -1):
            #print("I am j",j)
            if arr_list[j] > arr_list[j+1]:
                arr_list[j],arr_list[j+1] = arr_list[j+1], arr_list[j]
    return arr_list

print(insertionSort(arr_list2))            