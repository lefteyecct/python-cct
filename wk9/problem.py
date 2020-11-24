"""
Use map() to create a function which finds the length of each word in the phrase (broken by spaces) and returns the values in a list.

The function will have an input of a string, and output a list of integers.
"""

def word_lengths(phrase):    
    lst_word = str.split(phrase)
    print(list(map(len,lst_word)))

word_lengths('How long are the words in this phrase')

"""
Use reduce() to take a list of digits and return the number that they correspond to.
For example, [1, 2, 3] corresponds to one-hundred-twenty-three.
Do not convert the integers to strings!
"""

from functools import reduce

def digits_to_num(digits):    
    return print(reduce(lambda x,y:x*10 + y,digits))

digits_to_num([3,4,3,2,1])

"""
Use filter to return the words from a list of words which start with a target letter.
"""
def filter_words(word_list, letter):
    return print(list(filter(lambda word:word[0]==letter,word_list)))

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
filter_words(l,'h')