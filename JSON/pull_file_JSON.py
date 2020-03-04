# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:58:13 2020

@author: wisni
"""
import csv
import json

def retrieve_data(file_name):
    with open('pgh_capital_projects_official.csv') as dataset:
        data = csv.DictReader(dataset)
        id_list = []
        json_spec = []
        for row in data:
            id_list.append(row)
        return id_list
    
def retrieve_filter(json_file_pathway):
    '''
    With help from observing other individual's code from their Githubs,
    this will retrieve the filter from the .json file. I am still learning 
    so forgive me for any mistakes or errors. This is no way 100% my code. 
    '''
    with open(json_file_pathway) as json_file:
        json_data = json.load(json_file)
        new_filter = {}
        for i in json_data:
            if json_data[i] != '':
                new_filter.update( {i : json_data[i]} )
        return new_filter
    

def filter_project(listOfIds, a_filter):
    filtered_projects = []
    for i in listOfIds:
        count = 0
        jcount = len(a_filter)
        for e in a_filter:
            if a_filter[e] == i[e]:
                count += 1
        if count == jcount:
            filtered_projects.append(i)
    print(filtered_projects)
    return filtered_projects
    
def export_projects(filtered_projects):
    with open('capital_projects_filtered.csv', 'w', newline = '') as csv_file:
        sample_dict = filtered_projects[0]
        fieldnames = []
        for key in sample_dict:
            fieldnames.append(key)
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for p in filtered_projects:
            writer.writerow(p)
    print("A new csv file has been created with the filtered criteria.")
    



def main():
    '''
    The first variable retrieves the data set from 
    Capital Projects CSV
    The second variable retrieves the previously made json file with 
    the proper filters set (For this example, its all data for the year 2018)
    The third variable runs through th file and gets all the data for the year
    2018
    The last function exports the filtered projects to a csv file
    '''
    listOfIdeas = retrieve_data('pgh_capital_projects_official.csv')
    a_filter = retrieve_filter('capital_projects.json')
    filt_proj = filter_project(listOfIdeas, a_filter)
    export_projects(filt_proj)
main()