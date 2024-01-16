'''
Cole Johnson 1/15/2024
For CS 240 HW2
'''
'''
selection sort pseudo code

function def, needs to take an array as a parameter
    # needs a for loop to loop through each index in the array
    for i in range(len(array)) <- loops through each i index in array

        # need to find the smallest value between the current index and the end of the array
        min_idx = min_idx_function(array) <- some function than gets the min values index from the array

        swap array[i] and array[min_idx]

this works because you are finding the smallest value in the whole array and swapping it with the first index,
in the next iterations you are finding the next smallest value and swapping it with the second index,
this is repreated until you get to the final index.

because it is a nested for loop it has a big O of O(n^2) or quadratic time time complexity.
'''

# ========== function definitions ========== #

# function that creates an array of int values from a txt file
# same as the one used in HW1
def file_to_arr(fn):
    arr = []
    f = open(fn, 'r')
    for line in f.readlines():
        arr.append(int(line))
    f.close()
    return arr

# selection sort function
def selection_sort(arr):
    # loop through each element of the array
    for i in range(len(arr)): 
        # finds the min_index
        min_idx = i 
        # loops through each index 'above' the current index
        for j in range(i + 1, len(arr)): 
            # check if the current index being checked is less than the current lowest
            if (arr[min_idx] > arr[j]): 
                # if it is save it
                min_idx = j
        # now min_idx is the index of the smallest element above the current index
        # swap the current indexs element and the smallest element
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
        
# ========== main code ========== #

# selection sort with a small array
#arr1 = [1, 534, 232, 23, 4, 45]
#selection_sort(arr1)
#print(arr1)

# selection sort with a large array
arr2 = file_to_arr("numbers-1.txt")
selection_sort(arr2)
print(arr2[7586])