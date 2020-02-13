# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:23:00 2020

Eric's 10x10 Dragon Icon 
Hope ye enjoy! 

@author: wisni
"""

my_dictionary = {"1": [0,0,1,0,0,0,0,1,0,0],
                 "2": [0,1,0,0,0,1,0,0,1,0],
                 "3": [1,0,0,0,1,1,0,0,0,1],
                 "4": [1,0,0,0,0,1,0,0,0,1],
                 "5": [1,1,1,1,1,1,1,1,1,1],
                 "6": [1,0,0,0,1,1,0,0,0,1],
                 "7": [1,0,0,0,0,1,0,0,0,1],
                 "8": [0,1,0,0,1,0,0,0,1,0],
                 "9": [0,0,1,0,0,1,0,1,0,0],
                 "10": [0,0,0,0,1,1,0,0,0,0]
                     }
 

   
    
def create_dragon_icon(dictionary):
    '''
    reads in keys and values from dict.items(), then puts the values
    , which are the lists, one at a time, through the value brkdwn function
    '''
    for key,value in dictionary.items():
       value_break_down(value)
        
            
def value_break_down(a_list):
    '''
     creates a new list for new characters, then goes through the list,
     if the list does not have 1, then it will add 10 spaces to the new list,
     if not, then it will add a 0, all still being in same order.
     then it puts new list and 10 (whatever scaling number wanted) into 
     clear visual function
     '''
    new_list = []
    for item in a_list:
        if item != 1:
            for number in range(0,10,1):
                new_list.append(" ")
        else:
            for number in range(0,10,1):
                new_list.append("0")
    clear_visual(new_list,10)
    return new_list 


def clear_visual(b_list,scaling_number):
    '''
    this changes the list to a string, then it creats a new line that is one
    long string. after that it loops through the scaling number and prints
    them vertically
    '''
    str(b_list)
    new_string = ""
    new_string = ''.join(str(e) for e in b_list)
    for number in range(scaling_number):
        print(new_string, "\t")
    return new_string




    
    
def main():
    '''
    this puts the dictionary through the first function listed
    '''
    create_dragon_icon(my_dictionary)
        
main()