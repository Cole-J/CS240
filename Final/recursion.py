'''
Cole Johnson 3/17/24
For CS240 Final
'''

# ==================== convert to binary ==================== #

'''
function def, pass number
    if number is 0 return 0 as a base case
    else
        retrun 
            number mod 2 + 10 * recursive function call with parameters (integer of passed number / 2)  

function def
    binary = 0
    while the passed number > 0
        binary += number mod 2
        binary *= multi
        multi *= 10
        number /= 2
    return binary
'''

def convert_to_binary_r(number):
    # base case
    if number == 0:
        return 0
    # general case
    else:
        return (number % 2 + 10 * convert_to_binary_r(int(number // 2)))
    
def convert_to_binary_i(number):
    # if num is 0 return 0
    if number == 0:
        return 0
    # def variables
    binary_number = 0
    multiplier = 1
    # while number exists
    while number > 0:
        # calc for binary
        binary_number += (number % 2) * multiplier
        multiplier *= 10
        number //= 2
    # return binary
    return binary_number

#print(convert_to_binary_r(10))
#print(convert_to_binary_i(10))

'''
they have the same runtime however the recursive version is much simpler.

linear time complexity
'''
    
# ==================== finding the LCD ==================== #

'''
function def
    if greater exist and greater mod denominator is 0
    if no greater value find greater value
    return recursive function

function def
    get the greater of the 2 denominators
    while
        if greater mod denominator is 0
            lcd = greater
        greater ++
    return lcd
'''

def lcd_r(denom1, denom2, greater=None):
    # if greater mod of both denominator is 0 then return the value
    if greater is not None and greater % denom1 == 0 and greater % denom2 == 0:
        return greater
    # recursive case
    if greater is None:
        # start searching for the lcd with the greater of the 2 denominators
        greater = max(denom1, denom2)
    # return the result of the recursive call
    return lcd_r(denom1, denom2, greater + 1)

def lcd_i(denom1, denom2):
   # get the greater number
    greater = max(denom1, denom2)
    while(True):
        # if the greater mod of both denominator is 0 then return the value
        if((greater % denom1 == 0) and (greater % denom2 == 0)):
            return greater
        greater += 1

#print(lcd_r(5, 6))
#print(lcd_i(6, 5))
        
'''
they have the same time complexity as the greater value is being upped by 1 in both while searching.
both also start at the greater value when searching.

linear time complexity
'''

# ==================== exponent of x and e ==================== #
    
'''
function def
    if exponent is 0
        return 1
    if exponent is 1
        return passed x
    else
        return passed x * function (exponent - 1)

function def
    for each number of exponents
        multiply the passed number by itself
'''

def power_r(x, e):
    # base cases for e 0 and e 1
    if e == 0:
        return 1
    elif e == 1:
        return x
    # general case
    else:
        return x * power_r(x, e - 1)
    
def power_i(x, e):
    result = 1
    # for as many times as e multiply result by x to get x^e
    for _ in range(e):
        result *= x
    return result

#print(power_r(2, 4))
#print(power_i(2, 4))

'''
both will run for (e) times so they have the same time complexity with scales linearly by (e).

linear time complexity
'''