# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:33:47 2020

Regular Expressions Lesson

@author: wisni
"""

# Very Powerful
# Can pull out a string pattern 
# '\' - used to indicate special characters Ex: \n \t
# 'r' expression (raw string), voids Python's special characters 
# r'\n' means raw string with two characters 'n' and '\' instead of '\n'

import re

re.search('n', '\\n') # first item is pattern, second is string

re.search('n', r'\n\n\n\n\n\n\n\n\n') # use of r'string'

re.search(r'\n', '\n\n') # also looks for new line. if regex is r'\n',
                         # it doesn't affect it if its a metacharater

re.search(r'\n', r'\n\n') # looks for new line but since it's r'string',
                          # it doesn't use new line
                          
                          
# Common Methods for Regex
# Match and Search

re.search(pattern, string, flags) # searches anywhere in string, flags are
                                  # special options Ex: Ignore Capital, Deal
                                  # with multi-lines

re.match(pattern, string, flags) # searches the first character of string

re.match('c', "abcdef") # returns none due to the first character being 'a'

re.search('c', "abcdef") # gets match object 
                         # <_sre.SRE_Match object; span =(2,3), match='c'>

bool(re.match('c', "abcdef")) # no match, returns false

bool(re.match('a', "abcdef")) # match, returns true
                              # This is a good way to see if you are getting
                              # the match that you want in a string
                              
re.search('c', 'abcdefc') # the match object matches at the first point only
                          # so the second instance of 'c' gets left out
                    
re.search('c', 'abdef\nc') # multi-line works with search

re.search('c', 'abdef\nc') # match doesn't work with newline


# Printing the output of match and search

(re.match('a', 'abcdef')) # match objects

(re.match('a', 'abcdef')).group() # string output, default value is 0
                                  # pulls out the match string
                                                     
re.search('c', 'abdef\nc').start() # pulls out starting index

re.search('c', 'abdef\nc').end() # pulls out ending idex


# Literal Matching

re.search('c|d', 'abdefnc abcd') # c or d, can use as many as u want

# re.findall()

re.findall('n|a', 'bcdefnc avcda') # finds and pulls all instances as list

re.findall('abcd', 'abcdefnc abcd') # would pull out ['abcd','abcd']

# Character Sets

re.search(r'\w\w\w\w', 'abcdefnc abcd') # \w matches characters and numbers 

# \w matches alpha numeric characters [a-zA-Z0-9_], not symbols

re.search(r'\w\w\w', 'a22-_!').group # outputs string 'a22'

# \W is compliment of \w, meaning everything \w is not 

# Quantifiers

# '+' = 1 or more
# '?' = 0 or 1 (Use: What your looking for may or may not be there )
# '*' = 0 or more
# '{n,m}' = n to m repititions {,3} {3,}

re.search(r'\w+', 'abcdefnc abcd').group() # will go until it reaches a 
                                           # non alpha numeric number
                                           
                                           
re.search(r'\w+\W+\w+', 'abcdefnc abcd').group()   # will output full string
                                                   # '\W+' used to account for
                                                   # empty space in string.
                                                   # AttributeError if you 
                                                   # search \W+ and there
                                                   # are no non alpha numeric
                                                   # characters
            

re.search(r'\w+\W?\w+', 'abcdefncabcd').group()   # will account for any
                                                  # non alpha numeric if they
                                                  # are there
   
re.search(r'\w{3}', 'abcdefnc abcd').group() # 3 '\w'
                                     
re.search(r'\w{1,4}', 'abcdefnc abcd').group() # '\w' from 1-4

re.search(r'\w{1,}\W{0,}\w+', 'abcdefnc abcd').group() # would pull out whole 
                                                       # string Hint: Explain 
                                                       # {n,m}                                                     