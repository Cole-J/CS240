'''
Cole Johnson 2/5
For CS240
'''

# ========== pseudo code ========== #

'''
def partition function
    function to find the position of the partition

    default pivot is the rightmost index

    for x in range of the array
        compare the elements in the array to the pivots element

        if a element smaller than the pivot is found
            swap current element with element of pointer + 1

    swap pivot element with pointer + 1 element

    return pointer

def quick sort function
    get the pivot using partition function
    quick sort function with pivot - 1
    quick sort function with pivot + 1
'''

# ========== quick sort function ========== #

def partition_from_pivot(arr, low, high): # O(n)
    # right index is pivot
    pivot = arr[high]
    # create a pointer of a greater element
    pointer = low - 1
    # go through elements and compare to pointer
    for i in range(low, high):
        if (arr[i] <= pivot):
            # if element smaller than pivot swap with greater element
            pointer += 1
            arr[pointer], arr[i] = arr[i], arr[pointer]
    # swap pivot element with the pointer element
    arr[pointer + 1], arr[high] = arr[high], arr[pointer + 1]
    # return the position were the swap happend
    return pointer + 1

def quick_sort(arr, low, high): # O(n*log(n))
    if (low < high):
        pivot = partition_from_pivot(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def search(x, arr): # O(n) linear search function
    i = 0
    for e in arr:
        if (e == x):
            return i
        i += 1
    return -1 

# ========== main code ========== # 
        
# opens n4.txt and generates the array
arr = []
with open('numbers-4.txt', 'r') as fh:
    for i in [int(num) for num in fh.readlines()]:
        arr.append(i)
# quick sort the array
quick_sort(arr, 0, len(arr) - 1)
# check if the array is sorted
array_sorted = "is"
for i in range(len(arr)):
    if arr[i] < arr[i-1] and i > 2:
        array_sorted = "isnt"
# prints outputs
# uncomment the print(arr) to see the array data
#print(arr)
print(f"array {array_sorted} sorted")
print(search(90262, arr))
print(search(11559, arr))