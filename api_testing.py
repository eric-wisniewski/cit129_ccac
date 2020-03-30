# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:20:26 2020

@author: wisni
"""

import requests, json, re



def retrieve_json_from_api():
    '''
    Retrieves API from Github on positions available in the US
    In this function, we grap the actual data itself aswell as grab
    the Ids in each list item.
    
    '''
    req = requests.get("https://jobs.github.com/positions.json?description=python&full_time=true")
    if(int(req.status_code) == 200):
        apiDicts = json.loads(req.text)
        # print(apiDicts)
    return apiDicts


def total_counter(list_dict):
    '''
    This grabs the total amount of jobs 
    '''
    counter = 0
    for i in list_dict:
        for key in i:
            counter += 1
    print("For the Github Jobs api, there are a total of ",counter, "Jobs.\n")
    return counter
    
def get_list_of_all_types(list_in_dict): 
    '''
    
    This takes in the data and creates a list of all types for the user.
    
    The "# print" function shows the Full Time and Part Time list
    
    '''
    list_of_titles = []
    list_of_keys = []
    list_of_types = []
    for i in list_in_dict:
        for key in i:
            if i['title'] not in list_of_titles:
                list_of_titles.append(i['title'])
            if i['type'] not in list_of_keys:
                list_of_types.append(i['type'])
            if key not in list_of_keys:
                list_of_keys.append(key)
    # print(list_of_keys)
    return list_of_types

def get_list_of_titles(list_in_dict):
    '''
    
    This gets list of all titles for Regex
    
    '''
    list_of_titles = []
    for i in list_in_dict:
        for key in i:
            list_of_titles.append(i['title'])
    return list_of_titles
            

def get_list_of_companies(list_in_dict):
    '''
    This gathers list of 1 of each company
    '''
    list_of_companies = []
    for i in list_in_dict:
        for key in i:
            if i['company'] not in list_of_companies:
                    list_of_companies.append(i['company'])
    return list_of_companies

def get_list_of_all_companies(list_in_dict):
    '''
    This gathers all the companies for all jobs
    '''
    list_of_all_companies = []
    list_of_companies = []
    for i in list_in_dict:
        for key in i:
            if i['company'] not in list_of_companies:
                    list_of_all_companies.append(i['company'])
    return list_of_all_companies
        
                
def perc_of_f_vs_p(list_of_all_types):
    '''
    This finds the percentages of Part Time vs. Full Time
    '''
    print("For all of the jobs in api:")
    counter = 0
    full_time_counter = 0
    for i in list_of_all_types:
        counter += 1
        if i == 'Full Time':
            full_time_counter += 1
    perc_of_full_time = ((full_time_counter/counter)*100)
    perc_of_part_time = (100 - perc_of_full_time)
    print(perc_of_full_time,"% Full Time\n ", perc_of_part_time, \
          "% Part Time\n")


def display_jobs_for_companies(list_of_all_comp, list_of_comp):
    '''
    This displays how many of jobs belong to each company
    '''
    print("This table shows how many jobs are available for each company\n")
    print("#  : Company")
    for i in list_of_comp:
        counter = 0
        for j in list_of_all_comp:
            if i == j:
                counter += 1
        print(counter,":", i)          
            
        
def regex(list_of_titles):
    '''
    
    
    This takes in a list of 550 titles from the api and use the Regex 
    function re.findall('string', 'pattern')
    
    '''
    print("")
    list_eng = []
    list_dev = []
    list_sen = []
    for item in list_of_titles:
        list_eng += re.findall('Engineer', item)
        list_dev += re.findall('Developer', item)
        list_sen += re.findall('Senior', item)
    counter_eng = list_eng.count('Engineer')
    counter_dev = list_dev.count('Developer')
    counter_sen = list_sen.count('Senior')
    print("For the full list of 550 titles, the word 'Engineer' shows up in",  
counter_eng, "jobs, the word 'Developer' shows up in", counter_dev, \
"jobs, and the word 'Senior' shows up in" \
,counter_sen, "jobs.")

        
def main():
    jobs_dict = retrieve_json_from_api()
    list_o_types = get_list_of_all_types(jobs_dict)
    list_o_jobs = get_list_of_companies(jobs_dict)
    list_o_all_jobs = get_list_of_all_companies(jobs_dict)
    list_o_titles = get_list_of_titles(jobs_dict)
    
    total_counter(jobs_dict)
    
    perc_of_f_vs_p(list_o_types)
    
    display_jobs_for_companies(list_o_all_jobs, list_o_jobs)
    
    regex(list_o_titles)


    
    
main()