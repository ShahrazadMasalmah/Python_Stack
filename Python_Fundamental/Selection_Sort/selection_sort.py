arr_list = [8,5,2,6,9,3,1,4,0,7]

# Selection sort in Python
#sorting by finding min_index
def selectionSort(arr_list):
    
    for i in range(len(arr_list)):
        min_index = i
 
        for j in range(i + 1, len(arr_list)):
            # select the minimum element in every iteration
            if arr_list[j] < arr_list[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (arr_list[i], arr_list[min_index]) = (arr_list[min_index], arr_list[i])

    return arr_list    

print(selectionSort(arr_list))

