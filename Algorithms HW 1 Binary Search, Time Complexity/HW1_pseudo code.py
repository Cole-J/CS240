'''
Cole Johnson 1/9/2024
For CS 240 HW1
'''

'''
pseudo code for the bsa function

binary search function (parameters are the search_number and arr of numbers):
    define the starting low index at 0
    defines the starting high index as being the index at the end of the array
    
    while the low index is not equal to the high index

        define the mid index as being in the middle of the high and low indexs
        so that the mid is in the middle of the current array

        moving the low or high values will be used to cut off parts of the array

        if the element at the mid index matches the search_number return that index
            break the loop

        if the element at the mid index is less than the search_number
            we then know that we need to look above the mid index to find the number

            the new low index is the current mid index

            continue the loop

        if the element at the mid index is greater than the search_number
            we then know that we need to look below the mid index to find the number

            the new high index is the current mid index

            continue the loop

    if the loop runs until the low index is equal to the high index then the search_number could not
    be gound within the array

    return a null value

    

                                why this works

                                

each time the loop runs we are finding the current arrays mid index,
we then check if the number we are searching for is less, equal, or greater than that indexs element.

if the mid indexs element matches the search number we stop the loop and return the index

if the mid indexs element is less than the search number we 'cut' off the portion of the array below
that mid index.

if the mid indexs element is greater than the search number we do the reverse and 'cut' off the portion
of the array above the mid index.

each time we cut off a portion of the array it cuts the current array size in half allowing the desired
number to be found in about 11 operations as the txt file has 2000 entries (log_2 2000 ~ 11).
'''