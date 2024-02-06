'''
Cole Johnson 2/6
For CS240
'''

# hash function using honers method
def hash(key, base, mod):
    value = 0 # base value
    for char in key:
        value = (value * base + ord(char)) % mod # add the hash to the total value
    return value # return the total value

# some tests
print(hash("cole", 33, 10))
print(hash("henery", 33, 10))
print(hash("jason", 33, 10))
print(hash("stephon", 33, 10))