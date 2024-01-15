'''
Cole Johnson 1/9/2024
For CS 240 HW1

    general information about the program

the functions in the functions / main code part are as follows

the file_to_arr(fn) function creates an array of integers from a passed filename.
In this case its used to make an array of the numbers in "numbers.txt".
the parameter fn is the file name of the file.

the bsa(num, arr) function is a binary search algorithm while takes the parameters num, which
is the number you are searching for, and arr, which is the array of numbers your are searchig for
the num number in. it will return an tuple of 2 integers.
the first number in the tuple is the index of the element num in the array arr. if its -1 then no element
matching num was found, if its not -1 than that is the index of an element matching num in the array arr.
the second number in the tupe is the operations needed to find that data.

the print_data(search_int, arr) takes a integer (search_int) which you would like to search with the bsa
function and an array of integers (arr). it runs the bsa function and prints the outputted data to the
console.
'''


# ========== functions ========== #
# the functions used in the program to keep the main code simple


# function to create an array of the numbers in the txt file
def file_to_arr(fn):
    arr = [] # create an empty array
    f = open(fn, 'r') # open the file in read mode
    for line in f.readlines(): # for each line in the file
        arr.append(int(line)) # append the line after its converted to an integer
    f.close() # close the file
    return arr # return the full array


# function that does the binary search
def bsa(num, arr):
    low = 0 # the low index of the array is 0
    high = len(arr)-1 # the high index of the array is its last index
    op_count = 0 # variable to keep track of operations / times the loop has run

    while (low <= high): # loops while low is less than high
                         # this allows for an exit condition for when an index is not found
        op_count += 1 # add one to the operation count

        # calculate the middle index in the array and ensure its conversion to an integer
        mid = low + (high-low) // 2
        # if the middle indexs element is the target number
        if arr[mid] == num:
            return mid, op_count # return the middle index and the operations needed to find it
        # if the middle indexs element is less than the target number
        elif arr[mid] < num: # set the low as one above the current middle index
            low = mid + 1
        # if the middle indexs element is greater than the target number
        else:
            high = mid - 1 # set the high as one below the current middle index
    return -1, op_count # return -1 if there is no index for the target number


def print_data(search_int, arr): # small function to run the main code and print its data to the console
    # use the binary search function to get the index of a number in the array
    # function will return -1 if the number does not exist in the array
    idx, op = bsa(search_int, arr) # gets the data from the binary search
    # idx is the index it was found at and op is the number of operations
    if (idx != -1):
        # print on the condition an index was found
        print("the number " + str(search_int) + 
              " is in the " + str(idx) + " index of the array, or line " + str(idx+1) +
              ",\nthis data was found in " + str(op) + " operations\n")
    else:
        # print on the condition than an index was not found
        print("no element matching " + str(search_int) + " was found in the array,\n" + 
              "this data was found in " + str(op) + " operations\n")


# ========== main code ========== #

# get an array of the numbers in "numbers.txt"
arr = file_to_arr("numbers.txt")
arr.sort() # make sure the array is sorted

# print the wanted data
print_data(51216352, arr)
print_data(198313119, arr)
print_data(196614208, arr)