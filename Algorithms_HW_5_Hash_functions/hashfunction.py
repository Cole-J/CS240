'''
Cole Johnson 2/6
For CS240
'''

# hash function using honers method
def hash(key, base, mod):
    value = 0 # base value
    for char in key:
        value = (value * base + ord(char)) # add the hash to the total value
    return value % mod # return the total value

# some tests
print(hash("cole", 33, 100))
print(hash("henery", 33, 100))
print(hash("jason", 33, 100))
print(hash("stephon", 33, 100))