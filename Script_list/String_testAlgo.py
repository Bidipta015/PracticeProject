"""Define a function called stringmethod, which takes five parameters.

The first parameter is para, which takes a string sentence.
The second parameter is special1, which takes a string of special characters.
The third parameter is special2, which takes a single string of special characters.
The fourth parameter is list1, which takes a list of strings.
The fifth parameter is strfind, which takes a string.
The function definition code stub is given in the editor. Generate print statements based on the following conditions:

Remove all the special characters from para specified in special1 and save them in the variable word1.

Get the first 70 characters from word1, reverse the strings, save it in variable rword2, and print it.

Remove all the wide spaces from rword2, join the characters using the special character specified in special2, and print the joint string.

If every string in list1 is present in para, then format the print statement as follows:

"Every string in <list1> were present"
Else:
"Every string in <list1> were not present"
Split every word from word1 and print the first 20 strings as a list.

Calculate the less frequently used words whose count < 3, and print the last 20 less frequent words as a list.

Note: Count the words in the order that they appear.
Print the last index in word1, where the substring strfind is found. """

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


#
# Complete the 'strmethod' function below.
#
# The function accepts following parameters:
#  1. STRING para
#  2. STRING spch1
#  3. STRING spch2
#  4. LIST li1
#  5. STRING strf
#

def stringmethod(para, special1, special2, list1, strfind):
    word1 = para
    for char in special1:
        word1 = word1.replace(char, "")

    truncate_word1 = word1[:70]

    rword2 = truncate_word1[::-1]
    print(rword2)

    rword2_no_space = rword2.replace(" ", "")
    joined_rword2 = special2.join(rword2_no_space)
    print(joined_rword2)

    if all(item in para for item in list1):
        print(f"Every string in {list1} were present")
    else:
        print(f"Every string in {list1} were not present")

    word1_split = word1.split()
    print(word1_split[:20])

    word_counts = Counter(word1_split)
    less_frequent_words = [word for word, count in word_counts.items() if count < 3]
    print(less_frequent_words[-20:])

    last_index = word1.rfind(strfind)
    print(last_index)


if __name__ == '__main__':
    para = input()

    spch1 = input()

    spch2 = input()

    qw1_count = int(input().strip())

    qw1 = []

    for _ in range(qw1_count):
        qw1_item = input()
        qw1.append(qw1_item)

    strf = input()

    stringmethod(para, spch1, spch2, qw1, strf)
