# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 10:50:38 2023

more reference : https://www.geeksforgeeks.org/read-json-file-using-python/

"""
import json
fileName = '.\data\pax.json'

def load():
    with open(fileName) as user_file:
        parsed_json = json.load(user_file)
        return parsed_json['pax']

def addNewPax(new_data):
    with open(fileName,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["pax"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
    # python object to be appended


if __name__ == "__main__":
    '''
    data = load()
    for i in data:
        print(i)
        '''
    y = {"name":"Sam",
     "age": 40
    }
     
    addNewPax(y)
    
        