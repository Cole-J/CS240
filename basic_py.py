def file_to_arr(fn):
    arr = [] # create an empty array
    f = open(fn, 'r') # open the file in read mode
    for line in f.readlines(): # for each line in the file
        arr.append(int(line)) # append the line after its converted to an integer
    f.close() # close the file
    return arr # return the full array