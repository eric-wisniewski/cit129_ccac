# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 17:18:13 2020

@author: wisni
"""
import json
import csv


               

def capital_projects():
    '''
    Iteraters over City of Pittsburgh Capital Projects data
    
    Retrieved on 02-17-20
    https://data.wprdc.org/dataset/capital-projects
    '''
    with open('pgh_capital_projects_official.csv') as dataset:
        data = csv.DictReader(dataset)
        number_of_jobs_dict = {'Bridge':0,'Facility':0, "Non-Asset":0, \
                               'Playground':0, 'Playing Field':0, \
                               'Pool':0, 'Signalized Intersection':0, \
                               'Step':0, 'Retaining Wall':0, \
                               'Roofing System':0, 'Sidewalk':0, 'Court':0, \
                               'Pavement':0
                               }
        total_num_proj = 0
        list_of_asset_types = []
        for row in data:
            '''
            1) The first "if" statement totals all the projects in the csv
            2) The second "if" statement creates a list of all possible asset
            asset types
            3) The function after the second "if" statemnts calculates
            the percentages of all asset types and places them into a 
            dictionary
            4) 
            '''
            if row == row:
                total_num_proj += 1
            else:
                print("How'd You Get This?")
            
            if row['asset_type'] not in list_of_asset_types:
                list_of_asset_types.append(row['asset_type'])
            
            if row['asset_type'] == "Bridge":
                number_of_jobs_dict['Bridge'] += 1
            elif row['asset_type'] == "Facility":
                number_of_jobs_dict['Facility'] += 1
            elif row['asset_type'] == "Non-Asset":
                number_of_jobs_dict['Non-Asset'] += 1
            elif row['asset_type'] == "Playground":
                number_of_jobs_dict['Playground'] += 1
            elif row['asset_type'] == "Playing Field":
                number_of_jobs_dict['Playing Field'] += 1
            elif row['asset_type'] == "Pool":
                number_of_jobs_dict['Pool'] += 1
            elif row['asset_type'] == "Signalized Intersection":
                number_of_jobs_dict['Signalized Intersection'] += 1    
            elif row['asset_type'] == "Step":
                number_of_jobs_dict['Step'] += 1    
            elif row['asset_type'] == "Roofing System":
                number_of_jobs_dict['Roofing System'] += 1    
            elif row['asset_type'] == "Sidewalk":
                number_of_jobs_dict['Sidewalk'] += 1    
            elif row['asset_type'] == "Retaining Wall":
                number_of_jobs_dict['Retaining Wall'] += 1      
            elif row['asset_type'] == "Court":
                number_of_jobs_dict['Court'] += 1
            elif row['asset_type'] == "Pavement":
                number_of_jobs_dict['Pavement'] += 1   
    
        stats_on_assets(total_num_proj, number_of_jobs_dict, \
                        list_of_asset_types)


def stats_on_assets(tot_asset_types, asset_dict, list_of_assets):
    print("Percentages of the asset types for all Capital Projects in \
Pittsburgh.\n")
    for key in asset_dict:
        percentage_of_key = ((asset_dict[key]/tot_asset_types)*100)
        print(key, percentage_of_key,"%")
    return percentage_of_key



def main():
    capital_projects()
               
                
main()

















