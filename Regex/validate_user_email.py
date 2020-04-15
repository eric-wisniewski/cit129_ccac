# -*- coding: utf-8 -*-
"""
Created on Wed Mar 9 17:36:18 2020

@author: wisni
"""
import re

pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(.com|edu|net|org)"

user_input = input()

if(re.search(pattern, user_input)):
    print("valid_email")
else:
    print("invalid_email")
    
    
    
