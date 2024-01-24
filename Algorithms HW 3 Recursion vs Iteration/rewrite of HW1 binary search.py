'''
Cole Johnson 1/17/2024
For CS240
'''

# basic linear search function used to test the binary search function
def linear_search(target, arr):
    for i in range(len(arr)):
        if (arr[i] == target):
            return i
    return -1

# function to search an array with a recursive binary search algorithm
# parameters are the element to search for, the array, the low index in the array,
# the high index in the array, and the current number of operations
def bsa(element, arr, low, high, op_count):
    op_count += 1
    # case for overflow / if no element is found
    if (low > high):
        return -1, op_count
    mid = (low + high) // 2
    # case for if the element is found in the array
    if (arr[mid] == element):
        # return the elements index
        return mid, op_count
    # case for if the current element is below the target element
    elif (arr[mid] < element):
        low = mid + 1
    else:
    # case for if the current element is above the target element
        high = mid - 1
    # starts the recursion
    return bsa(element, arr, low, high, op_count)

# function to call the binary search function and print its output
# parameters are an element to search for and the array to search in
def print_data(element, arr):
    # gets the index and the number of times it took to get to that index
    idx, opc = bsa(element, arr, 0, len(arr), 0)
    # if no index was found
    if (idx == -1):
        print("element " + str(element) + " not found in array in " + str(opc) + " operations")
    # if an index was found
    else:
        print("element " + str(element) + " found at index " + str(idx) + " in " + str(opc) + " operations")

# create an array from the txt file
arr = []
with open('numbers-3.txt', 'r') as fh:
    for i in [int(num) for num in fh.readlines()]:
        arr.append(i)
arr.sort()

# print the wanted data using the print data function
print_data(8128705, arr)
print_data(584219, arr)