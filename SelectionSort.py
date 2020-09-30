# Selection sort is a sorting function that finds the minimum element 
# from the unsorted part of the array(i.e right) and moves it to the 
# sorted part the array(i.e left)

def selectionSort(arr):
    for i in range(len(arr)-1):
        #initially we take i as index that has the minimum value
        min = i 
        #then we search the part of the array after this index
        for j in range(i+1, len(arr)):  
            #if we find an index whose value is less than that at min then
            if arr[j]<arr[min]: 
                #we assign this index as the index that has the minimum value 
                min = j  
        #after the this loop we place the element at min index at its respective position
        arr[min], arr[i] = arr[i], arr[min]

A = list(map(int, input('Please enter your array:\n').split())) #enter array as space separated integers
print('\nThe array after selection sort is: \n') 
selectionSort(A)
print(A)

