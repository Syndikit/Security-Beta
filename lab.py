
# coding: utf-8

# In[26]:


"""
Test variables initialized
"""
text = "password"
block_size = 8
#block_bitsize = 64
bit_list = list()
str_list = []
key_list = []


# In[27]:


init_permut_table = [58, 50, 42, 34, 26, 18, 10, 2,
                     60, 52, 44, 36, 28, 20, 12, 4,
                     62, 54, 46, 38, 30, 22, 14, 6,
                     64, 56, 48, 40, 32, 24, 16, 8,
                     57, 49, 41, 33, 25, 17, 9, 1,
                     59, 51, 43, 35, 27, 19, 11, 3,
                     61, 53, 45, 37, 29, 21, 13, 5,
                     63, 55, 47, 39, 31, 23, 15, 7]

permutation_key1 = [57, 49, 41, 33, 25, 17, 9,
                   1, 58, 50, 42, 34, 26, 18,
                   10, 2, 59, 51, 43, 35, 27,
                   19, 11, 3, 60, 52, 44, 36,
                   63, 55, 47, 39, 31, 23, 15,
                   7, 62, 54, 46, 38, 30, 22,
                   14, 6, 61, 53, 45, 37, 29,
                   21, 13, 5, 28, 20, 12, 4]

permutation_key2 = [14, 17, 11, 24, 1, 5, 3, 28,
                    15, 6, 21, 10, 23, 19, 12, 4,
                    26, 8, 16, 7, 27, 20, 13, 2,
                    41, 52, 31, 37, 47, 55, 30, 40,
                    51, 45, 33, 48, 44, 49, 39, 56,
                    34, 53, 46, 42, 50, 36, 29, 32]

expand_matrix = [32, 1, 2, 3, 4, 5,
                 4, 5, 6, 7, 8, 9,
                 8, 9, 10, 11, 12, 13,
                 12, 13, 14, 15, 16, 17,
                 16, 17, 18, 19, 20, 21,
                 20, 21, 22, 23, 24, 25,
                 24, 25, 26, 27, 28, 29,
                 28, 29, 30, 31, 32, 1]

left_shift_sched = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

post_sub_permut = [16, 7, 20, 21, 29, 12, 28, 17,
                   1, 15, 23, 26, 5, 18, 31, 10,
                   2, 8, 24, 14, 32, 27, 3, 9,
                   19, 13, 30, 6, 22, 11, 4, 25]

#Copy and pasted from the FIPS 46-3 Appendix pages 17-18
subs = [
#Substitution 1         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],
#Substitution 2
[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],
#Substitution 3
[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],
#Substitution 4
[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  
#Substitution 5
[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 
#Substitution 6
[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 
#Substitution 7
[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
#Substitution 8  
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]

final_permut_table = [40, 8, 48, 16, 56, 24, 64, 32,
                      39, 7, 47, 15, 55, 23, 63, 31,
                      38, 6, 46, 14, 54, 22, 62, 30,
                      37, 5, 45, 13, 53, 21, 61, 29,
                      36, 4, 44, 12, 52, 20, 60, 28,
                      35, 3, 43, 11, 51, 19, 59, 27,
                      34, 2, 42, 10, 50, 18, 58, 26,
                      33, 1, 41, 9, 49, 17, 57, 25]


# In[28]:


"""
Method for adding padding to message which may or may not be necessary, depending on message length.
Adds '00000000' elements to the list of binary letters of original message.
Input: message/ text to be padded to get length; list of binary letters to be added to. 
Output: appended list of letters that is now divisible by 8 with no remainder
"""
def padding(text, s_list):
    str_len = len(text)
    padding_needed = 8-(str_len%block_size) # Determines number of bytes of '00000000' to be added
    while padding_needed >0:
            s_list.append(bin(int('00',base=16))[2:].zfill(8)) #adds each all zero block to the input list
            padding_needed -= 1 #Updates the number of blocks still necessary
    return s_list


# In[29]:


"""
Converts ASCHII text to binary representation, 
formatting the strings returned by removing the '0b' and adding padding to the message as needed.
Input: text given such as message to be encrypted or password
Output: list of individual text letters converted to binary representation
"""
def str_to_bin(text):
    str_len = len(text)
    padding_needed = 8-(str_len%block_size)
    for i in range(0,str_len):
        c = ord(text[i]) # gives integer representation of the letter from text
        str_list.append(bin(c)[2:].zfill(8)) # formats binary letters as described above.
    if padding_needed > 0:
        #i = len(str_list)-1
        padding(text,str_list)
    return str_list


# In[30]:


"""
Creates the blocks of 64 bits of the message to be encrypted
Takes in the list of letters that were converted to binary as input and appends every 8 bytes to an empty block string.
Outputs a list of 8 byte blocks stored in lists. Basically, a list of lists.
"""
def make_blocks(str_list):
    num_bytes = len(str_list) #gets the length of the list of binary message letters
    num_blocks = num_bytes//block_size  # ensures the number of blocks to make is an 
                                        #integer value for the range function below
    start = 0
    end = 8
    for i in range(0,num_blocks):
        block = "" # ensures the block variable starts new every round of the for loop
        for j in range(start,end):
            block += str_list[j]
            
        start += 8 #increments the start variable by 8 due to the length of each block
        end += 8 #same as the start variable
        bit_list.append(block) # bit_list is a global variable at the top for storing these blocks.
        


# In[31]:


str_to_bin(text)
make_blocks(str_list)

print(bit_list)


# In[32]:


"""
Splits a block in to halves. DES doesn't use thirds or any other fraction of a block prior to splitting, so this method
can be used for any block size that needs to be split
Input: a string of some size that needs to be halved
Output: a list, consisting of each half stored as an element
"""
def split(block_28):
    block_len = len(block)
    half_len = len(block_28)/2
    c_and_d = list()
    c0 = block_28[0:half_len-1]
    d0 = block_28[half_len:block_len-1]
    c_and_d.append(c0)
    c_and_d.append(d0)
    return c_and_d


# In[33]:


"""
Performs the left shift operation on the string of bits given by converting them to an integer, 
then shifting by the number of bits given by the num_shifts attribute (depends on schedule) and 
ensuring the length is the same as the original block length
Input: string of bits; number of left shifts
Output: string of binary representation formatted to be the same length as original and with '0b' cleaved. 
"""
def left_shift(block, num_shifts):
    b_len = len(block)
    i = int(block)
    return bin(i << num_shifts)[2:].zfill(b_len)


# In[34]:


"""
Permuts a given block of bits based on a table given.
Input: block string to be iterated over; table with indices of bits to place in output string
Output: permuted string of bits
"""
def permut(block, table):
    perm_str = ""
    for i in table:
        perm_str += block[i-1]
    return perm_str


# In[35]:


"""
Generates all 16 subkeys and stores them in the global key_list variable. 
In each round, the concatenated c and d variables from the FIPS diagram 
are created by splitting a global permutation string, then left-shifted after separation, then recombined and permuted 
with Permutation Key 2. Recursive calls to the split(), left_shift(), and permut() are used.
Input: No attributes used. This method uses global variables and is only performed on one block, the key given from input.
Output: the key_list is populated with keys
"""
test_block = bit_list[0]
perm_str = permut(test_block,permutation_key1)

def generate_keys():
    for i in range(16):
        c_and_d = split(perm_str)
        c0 = left_shift(c_and_d[0], left_shift_sched[i])
        d0 = left_shift(c_and_d[1], left_shift_sched[i])
        c_and_d = permut(c0,permutation_key2) + permut(d0,permutation_key2)
        key_list.append(c_and_d)


print(key_list)


# In[ ]:


"""
Main method for running the script
"""
def main(self,key, message, mode):
    encrypt = 1
    decrypt = 0 
    self.key = key
    self.message = message
    self.mode = encrypt
    
    
if __name__ == "__main__":
    main()


# In[17]:


"""
TESTING CELL
"""
# Gives the padded all zero bytes for each block
print(bin(int('00',base=16))[2:].zfill(8))

# Prints the length of the current list of bytes in memory
print(len(str_list))

# Prints list of message letters converted to binary and padded resulting from the str_to_bin()
print(str_to_bin(text))

# Prints the list of 8 byte blocks of binary
print(bit_list)


# In[32]:


"""
***DEPRECATED***
Simple, string-based left shift taking the substring and appending 
the first bit to the end of the new shifted string.
"""
shifted = test_block[1:28]
single_shift = test_block[0]
shifted += single_shift
print(test_block)
print(shifted)


# In[50]:


"""
***DEPRECATED***
Tests permutation algorithm for permuting later
"""
new_str = ""
permut = [3,1,5,4,7,2,6,11,10,8,9]
for i in permut:
    new_str += text[i-1]
print(new_str)

