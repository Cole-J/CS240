'''
Cole Johnson 3/17/24
For CS240 Final
'''

# using 
# https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-no-swears.txt
# for word reference

# import the hash table
from imports.hashtable_via_linkedlists import hashtable_linkedlist

class SPELLCHECK:
    # init function with the parameters
    # hash table size
    # hash table base and mode
    # and the threshold for finding words close to another
    def __init__(self, size, base, mod, threshold): # O(n) -> O(threshold)
        self.hash_table = hashtable_linkedlist(size, base, mod) # create table
        self.threshold = threshold
        self.min_max_array = [] # create a array with the range [-threshold to threshold] without 0
        for i in range(0-threshold, threshold + 1, 1):
            self.min_max_array.append(i)
        self.min_max_array.remove(0)

    # function to add a word to the table
    def add_word(self, word): # O(1) -> O(n)
        self.hash_table.add(word, word)

    # function to get the edit distance of 2 strings
    def levenshtein_distance(self, str1, str2): # O(n)
        len_str1 = len(str1) + 1
        len_str2 = len(str2) + 1
        # initialize a matrix to store the distances
        matrix = [[0 for _ in range(len_str2)] for _ in range(len_str1)]
        # initialize the first row and column
        for i in range(len_str1):
            matrix[i][0] = i
        for j in range(len_str2):
            matrix[0][j] = j
        # fill in the matrix based on the levenshtein distance algorithm
        for i in range(1, len_str1):
            for j in range(1, len_str2):
                cost = 0 if str1[i - 1] == str2[j - 1] else 1
                matrix[i][j] = min(
                    matrix[i - 1][j] + 1, # deletion
                    matrix[i][j - 1] + 1, # tnsertion
                    matrix[i - 1][j - 1] + cost # substitution
                )
        # the bottom-right cell of the matrix contains the levenshtein distance
        return matrix[len_str1 - 1][len_str2 - 1]

    # function that creates an array of keys close to a passed key
    def find_closest_entry(self, known_key): # O(1) -> O(n)
        closest_entry_array = [] # create empty array
        for i in self.min_max_array: # for each index that is +- the threshold
            hash_value = self.hash_table.hash(known_key) + i # create the known hash +- threshold
            node = self.hash_table.get_hash_node(hash_value) # get the root node of the list
            while node:
                # loop through each node in the list and check its edit distance
                if (self.levenshtein_distance(known_key, node.key) <= self.threshold):
                    # append to the array if its edit distance is within the threshold
                    closest_entry_array.append(node.key)
                node = node.next
        # return the complete array or None
        if closest_entry_array:
            return closest_entry_array
        return None

    # function to run the user interface
    def run(self):
        while True: # main while loop
            # main input
            # user can either check spelling in an array
            # add word to dict
            # quit
            print("do you want to check an input (c) add a new word (a), or quit the program (q)", end=' ')
            ipt = input().lower()
            # quit case
            if ipt == "q":
                print("ending program\n")
                break
            # add case
            elif ipt == "a":
                # gets the new word
                print("what word:", end=' ')
                new_word = input()
                # filters the word
                filtered_word = ''.join(char for char in new_word if char.isalpha()).lower()
                # adds the word
                self.add_word(filtered_word)
                print(f"added '{filtered_word}'\n")
            # check spelling case
            elif ipt == "c":
                # gets string
                print("what string do you want to test:", end=' ')
                string = input()
                # generates array from string
                word_array = string.split(' ')
                # filters each work in the array
                filtered_array = []
                for word in word_array:
                    new_word = ''.join(char for char in word if char.isalpha()).lower()
                    if new_word != "":
                        filtered_array.append(new_word)
                print()
                # current word = filtered_array[i]
                # loop through each word in the filtered array
                for i in range(len(filtered_array)):
                    # check if it exists in the hash table
                    if self.hash_table.get(filtered_array[i]) is None:
                        print(f"{filtered_array[i]} is not in the dictionary")
                        # if it is not in the table get an array of words close to it
                        closest_entry_array = self.find_closest_entry(filtered_array[i])
                        if closest_entry_array is not None:
                            # if close words could be found
                            print("(a to add the word, y to accept suggestion, n to not accept suggestion, q to stop suggestions)")
                            for closest_entry in closest_entry_array:
                                # for each close word
                                print(f"would you like to replace '{filtered_array[i]}' with '{closest_entry}'")
                                change = input().lower()
                                # quit case
                                if change == 'q':
                                    break
                                # add case
                                elif change == 'a':
                                    # adds word to dict
                                    self.add_word(word)
                                    break
                                # case for accepting word
                                elif change == 'y':
                                    print(f"'{filtered_array[i]}' is now '{closest_entry}'")
                                    # set the close word to the current word
                                    filtered_array[i] = closest_entry
                                    break
                        else:
                            print(f"could not find any words similar to '{filtered_array[i]}'")
                        print()
                # print the final string
                print("your resulting string is: ")
                print(' '.join(filtered_array))
                print()
# create spellcheck class
spellcheck = SPELLCHECK(100, 10000000, 31, 3)
# open the txt file and add the words to the dict
with open('google-10000-english-no-swears.txt', 'r') as f:
    for i in [str(word) for word in f.readlines()]:
        # each word as a \n in it so it has to be removed
        spellcheck.add_word(i[:len(i) - 1])
# run the ui loop
spellcheck.run()