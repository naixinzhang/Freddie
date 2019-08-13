################################# NY HOSPITALS #################################
#
# Title: Freddie
# Files: cleaning.py,hospitalsNY.py,input.py, main.py,path.py,regression.py,statistics.py,test_2.py,test.py

#
# Author:Naixin Zhang
# Email:nzhang228@wisc.edu
#
############################### OUTSIDE HELP CREDITS ###########################
#
# Persons: Cornelia Ilin
# Online sources: available in README file
#
############################### 80 COLUMNS WIDE ################################
import csv
import numpy as np
import pandas as pd
import os

'''
# The input.py script read data from input/RawData using three formates
'''


def read_data(file_names, data_structure, input_path):
    '''
    # this function reads in data (file_names)
    # the desired data structure is provided by the user
    # the desired data structure can be list(csv), array (numpy), dataframe(pandas)
    # if the user enters a data structure other than the ones listed above, Freddie
    # responds "I don't know how to read this data structure"
    # @param: file_names, data_structure, input_path
    '''
    file_names_list = file_names.split(",")
    for i in range(len(file_names_list)):
        if not os.path.isfile(os.path.join(input_path,file_names_list[i])):
            print("Wrong file names")
            return False, ""

    if data_structure != 'list(csv)' and data_structure != 'array(numpy)' and data_structure != 'dataframe(pandas)':
        print("I don't know how to read this data structure")
        return False, ""
    
    data_raw = []
    
    if data_structure == 'list(csv)':
        for filename in file_names_list:
            with open(os.path.join(input_path, filename), 'r') as f:
                reader = csv.reader(f, delimiter=",")
                data_raw.append(list(reader))
        return True, data_raw
    if data_structure == 'array(numpy)':
        for filename in file_names_list:
            data_raw.append(np.genfromtxt(os.path.join(input_path, filename),delimiter=','))
    if data_structure == 'dataframe(pandas)':
        for filename in file_names_list:
            df = pd.read_csv(os.path.join(input_path, filename), index_col = None, header = 0, low_memory = False)
            data_raw.append(df)
    return True, data_raw