'''
Cole Johnson 1/17/2024
For CS240
'''
'''
pseudo code for recursive linear search

function def, paramenters are the element and the array and the current index which starts at 0
    # need a case for if the current index is greater than length to prevent error
    if len(array) < index:
        # return a number to show that a number was not found
    
    # need a case for if the current element matches the element in the parameter
    if array[current index] = search element:
        # we know that the current index is the index of the search element
        return current index

    # case for if the current index does not match the search element
    current index = current index + 1
    return search function with the parameters element, array, and current index
    # the above will call the same function but the current index will be one greater
'''


# recursive linear search function
# takes a search element and an array as parameters
# returns the index that the element was found in the array or -1 if it was not found
def search(element, arr, start_idx = 0): # O(n) linear time complexity
    # case if the current idx is greater than the length of the array
    if (len(arr) <= start_idx):
        return -1
    # case if the current idx's element matches the search element
    elif (arr[start_idx] == element):
        return start_idx
    # starts recursion with a 1 greater search index
    return search(element, arr, start_idx + 1)


# main code to test the search function
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(search(0, arr))
print(search(7, arr))
print(search(-1, arr))
print(search(10, arr))