'''
Cole Johnson 1/15/2024
For CS 240 HW2
'''
'''
insertion sort pseudo code

function def, needs to take an array as a parameter
    # needs a for loop to loop through each index after the first in the array
    for i in range(1, len(array)) <- loops through each i index after the first in array

        # save the current element
        element = array[i]

        # while loop to loop backwards in the array
        # it needs to loop while an array elements exists / (count variable above -1)
        # and while the saved element is is less than the current indexs element

        j = i-1 # start at the index to the left of the current index

        # the first check passively excludes cases where the variable to the left is in the right place,
        # while also checking in later iterations if the saved element is less than the current element.
        # the second check makes sure that you dont go out of the arrays range.
        while (element < arr[j] and j >= 0)
                # in the loop the current element needs to be moved to the right and the
                # element being sorted to the left

                # move an elements index to the right of the count variable (j)
                arr[j + 1] = arr[j]

                # move the 'search' to the left to keep looking for a smaller variable
                j -= 1

        # exits the while loop when nothing to the left of j is less than the saved element

        # sets the saved element to its new place in the array (right of j)
        arr[j + 1] = element

this works because for each element (after the first as you cant move back from the first index) you
are checking if it is less than the element to its left.
if it is you loop to the left to find where it is no longer less than the element to its left.
as you loop to the left you also are properly swapping the variables.

because it is a nested loop it has a big O of O(n^2) or quadratic time time complexity.
its best case will be when the array is already sorted.
the worst case will be when the array is in reverse order.
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

# insertion sort function
def insertion_sort(arr):
    # loop through each element after the first in an array
    for i in range(1, len(arr)):
        # save the current element
        element = arr[i]
        j = i - 1
        # while loop to loop backwards through the array until
        # count (j) equals 0 / the count is at the begininng of the array
        # or the saved element is less than the current element
        while (j >= 0 and element < arr[j]):
                # move current element to the right
                arr[j + 1] = arr[j]
                # move what element is being searched to the left
                j -= 1
        # assign the saved element once its proper place is found (right of j)
        arr[j + 1] = element

# ========== main code ========== #

# insertion sort with a small array
#arr1 = [14, 53, 32, 3, 1, 564]
#insertion_sort(arr1)
#print(arr1)

# insertion sort with a large array
arr2 = file_to_arr("numbers-1.txt")
insertion_sort(arr2)
print(arr2[7586])