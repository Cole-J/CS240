'''
Cole Johnson 2/5
For CS240
'''

# ========== pseudo code ========== #

'''
def merge sort function(array)
    if the length of the array is greater than 1
        
        split into left and right arrays

        merge sort function(left array)
        merge sort function(right array)

        now we have arrays of 2 indexes and work back up to the full arrays

        sort each half by checking its values

        have the smaller sent to the left and greater sent to the right
'''
# ========== merge sort function ========== #

def merge_sort_function(arr): # O(n*log(n))
    # check that the length is greater than 1
    if (len(arr) > 1):
        # get the mid point in the array
        mid = len(arr)//2
        # divide into its left and right parts
        l_arr = arr[:mid]
        r_arr = arr[mid:]
        # recursive sort for each half
        merge_sort_function(l_arr)
        merge_sort_function(r_arr)

        i = 0 # variables for the following loops
        j = 0
        k = 0

        # loop through left and right sides
        while (i < len(l_arr) and j < len(r_arr)):
            #if the left side is less than right side
            if (l_arr[i] <= r_arr[j]):
                arr[k] = l_arr[i]
                i += 1
            else:
                # if the right side is less than right side
                arr[k] = r_arr[j]
                j += 1
            k += 1
        # make sure that all indexs were checked
        while (i < len(l_arr)):
            arr[k] = l_arr[i]
            i += 1
            k += 1
        while (j < len(r_arr)):
            arr[k] = r_arr[j]
            j += 1
            k += 1

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
# merge sort the array
merge_sort_function(arr)
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