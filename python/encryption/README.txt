Programming Environment:

1) Language: Python 3.5
2) Written on MacOSX in a Jupyter Notebook, then downloaded as a .py file
3) Libraries: re 
4) System resources: 8GB RAM

Approach: Algorithms and Design

Resources: FIPS 46-3, DES lecture PowerPoints and discussions with Dr. Goseva-Popstojanova, YouTube channels explaining DES steps and symmetric encryption (specific links found below)

Algorithms:
1) Cleaning Method:
    Purpose: Remove all incidental/ superfluous characters (non-alphanumeric) and spaces. Uses re library to perform regex                      operation to remove the undesired elements previously mentioned. 
    Input: String from text file before preprocessing/ password given (used in the password validation method, below)
    Output: Only alphanumeric string for further pre-processing
    
2) Password Validation:
    Purpose: Ensure the key to be used is long enough and consists of valid characters, after text cleaning
    Input: String from user keyboard input
    Output: Original key string to be used for subsequent permutations from permutation tables stored as lists of bit indices

3) Converting Text String to Binary:
    Purpose: Convert string of characters to formatted binary 8 bit representation and fill zeroes to the left as necessary
    Input: Cleaned message/ key strings
    Output: List of binary representations of the characters given.
    
4) 64-bit Block Builder:
    Purpose: Segment message/ key in to 64 bit blocks for permutations. Last pre-processing step (unless you count permutations). 
    Input: Individual bytes in a list 
    Output: List of 64-bit blocks stored as strings in that list
    
5) Permutation Method:
    Purpose: Contract/ expand key/message blocks to be used in key generation and processing
             Kept generic enough to be used in multiple calls, depending on the table needed/ step. 
    Input: The bit_list to be iterated over and the table to be used. 
    Output: newly permuted list of bit strings. 
   
6) Key Generation:
    Purpose: generate all of the keys and store them in order, in the key_list array
    Input: 64-bit block of binary, stored as a string
    Output: list of 16 subkeys after permutations and left shifts

Design:

1) My DES implementation broke the process in to three segments: Pre-processing, Key Generation, and Message Recombination
2) Each of these segments consisted of smaller steps such as cleaning text/ converting text, permuting bits/ strings, and printing results. 
3) Without using cryptographic libraries, the permutation keys and schedules needed to be stored in lists that could be iterated over to avoid duplication of code, where possible. This program was tested for each method, using the testcase.txt files provided, hard-coded samples, and input from the keyboard to ensure quality. Several iterations of methods such as left shifting and permuting were tried and the most readable options were chosen. Initially, splitting and left-shifting were done in the same method, but this proved problematic when called during key generation. Since the decryption method is just the encryption method in reverse, only one run method needed to be developed and the inputs would be a simple re-ordering from a list. 
