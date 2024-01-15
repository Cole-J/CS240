def binary_search(input, item):
    low = 0                
    high = len(input) - 1  
    count = 0
    # uses mid index to "zoom in" on item value
    while low <= high:  
        count += 1
        mid = (low + high) // 2                
        guess = input[mid]
        if guess == item:
            return mid, count  
        # excludes item values above midpoint from consideration
        if guess > item:
            high = mid - 1
        # excludes item values below midpoint from consideration
        else:
            low = mid + 1
    return None            
start = [1, 3, 5, 7, 9, 11, 13, 15, 17]

print(binary_search(start, 12))