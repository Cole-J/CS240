'''
Cole Johnson 1/17/2024
For CS240
'''

# ========== old code ========== #

# function to search for a sublist in a list
def search_for_sublist(main, sub):
    sub_len = len(sub)
    for i in range(len(main) - sub_len + 1):
        # checks if i + sub_len is equal to that portion of the main array
        if main[i : i + sub_len] == sub:
            return True
    return False

# ========== new code ========== #

def search_for_sublist_recursive(main, sub, i=0, j=0):
    # sublist found in main array
    if j == len(sub):
        return True
    # sublist not found in main array
    if i == len(main):
        return False

    # current element matches an element in sub array
    if main[i] == sub[j]:
        return search_for_sublist_recursive(main, sub, i+1, j+1)
    # current element does not match element for sub array
    else:
        return search_for_sublist_recursive(main, sub, i+1, 0)

# ========== main code ========== #
    
main_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_array = [6, 7, 8]

print(search_for_sublist(main_array, sub_array))
print(search_for_sublist_recursive(main_array, sub_array))