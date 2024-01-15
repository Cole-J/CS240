'''
Cole Johnson 1/9/2024
For CS 240 HW1
'''

# this is the bsa functions from the main code which does the actual binary search
# this copy has no comments as it is used to determine a time complexity function

def bsa(num, arr): # => O(1)
    low = 0 # => O(1)
    high = len(arr)-1 # => O(1)
    op_count = 0 # => O(1)

    while (low <= high): # => O(1)
        op_count += 1 # => O(1)*log n

        mid = low + (high-low) // 2 # => O(1)*log n

        if arr[mid] == num: # => O(1)*log n
            return (mid, op_count) # => O(1)*log n

        elif arr[mid] < num: # => O(1)*log n
            low = mid + 1 # => O(1)*log n

        else: # => O(1)*log n
            high = mid - 1 # => O(1)*log n
    return (-1, op_count) # => O(1)

# the stuff inside the while loop is O(1)*log n becuase the amount of the array
# being searched is being cut in half every loop

# the time complexity is
# T(n) = O(1)*log_2(n) + O(1) => T(n) = O(log_2 n) or O(log n)
# it is logarithmic time


# the next 2 functions are from part 4


''' # part a

function sum(arr){ # => O(1)
  counter = 0 # => O(1)

  for (i = 0; i < arr.length; i++) { # => O(1)
       counter += arr[i] # => O(1)*n
  }

     return counter # => O(1)
} 

the time complexity is 
T(n) = O(1) + O(1) + O(1) + O(1)*n + O(1) => T(n) = O(1)*n => T(n) = O(n)
'''


''' # part b

function getXOR(arr1, arr2){ # => O(1)

  arr3 = [] # => O(1)

  for (i = 0; i < arr1.length; i++){ # => O(1)
      let unique = True # => O(1)*n
      for (j = 0; j < arr2.length; j++ }{ # => O(1)*n
        if(arr1[i] == arr2[j]) {unique = False;} # => O(1)*n*n
      }
      if (unique) {arr3.append(arr1[i]);} # => O(1)*n
    }
  }  
  for (i = 0; i < arr2.length; i++){ # => O(1)
    let unique = True # => O(1)*n
    for (j = 0; j < arr1.length; j++ }{ # => O(1)*n
      if(arr2[i] == arr1[j]) {unique = False;} # => O(1)*n*n
    }
    if (unique) {arr3.append(arr2[i]);} # => O(1)*n
  }
  return arr[3] # => O(1)
}

the time complexity is
T(n) = O(1)*n^2 + O(1)*n + O(1) => T(n) = O(1)*n^2 => T(n) = O(n^2)
'''