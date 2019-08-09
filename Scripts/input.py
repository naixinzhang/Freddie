################################# NY HOSPITALS #################################
#
# Title:
# Files: 
#
# Author:
# Email:
#
############################### OUTSIDE HELP CREDITS ###########################
#
# Persons: Cornelia Ilin
# Online sources:
#
############################### 80 COLUMNS WIDE ################################
import csv
import numpy as np
import pandas as pd
import os


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
        with open(os.path.join(input_path, file_names), 'rU') as file:
            data_csv= csv.reader(file_names, delimiter=",")
            return True, data_csv
    
    if data_structure == 'array(numpy)':
        data_numpy = np.genfromtxt(os.path.join(input_path, file_names),delimiter=',')
    
    if data_structure == 'dataframe(pandas)':
        for filename in file_names_list:
            df = pd.read_csv(os.path.join(input_path, filename), index_col = None, header = 0)
            data_raw.append(df)
    return True, data_raw