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

import pandas as pd
from prettytable import PrettyTable
import os


'''
# The cleaning.py script holds mainly for data summarize and data cleaning
'''

def row_col_number(data_raw,data_structure):
    '''
    # this function aims to get the raw data's shape
    # @param: data_raw is the original data including three years data 
    '''
    print("Ok, good choice. Tell me what you would like to do next?")
    input(">: ")
    rows = 0
    columns = 0
    if data_structure == 'dataframe(pandas)':
        for i in range(len(data_raw)):
            rows = rows + len(data_raw[i].index)
            columns = columns + len(data_raw[i].columns)
    elif data_structure == 'list(csv)':
        rows = len(data_raw)
        columns = len(data_raw[0])
    print("Let me check...oh...this data is really big!")
    print("You have %d inpatient discharges and %d variables that documnet these observations" % (rows, columns))

def remove_missing_value(data_raw,data_structure):
    
    '''
    # this function aims to deal with missing value
    # @param: data_raw is the original data including three years data 
    '''

    
    input(">: ")
    print("No problem, I can help you with this. Let's clean the data first.")
    print("Would you like to drop observations with missing values?")
    input(">: ")
    
    data_no_nan = []
    
    if data_structure == 'dataframe(pandas)':
        for i in range(len(data_raw)): 
            if i == 0:
                data_no_nan.append(data_raw[i].dropna(subset = ['Health Service Area', 'Hospital County', 'Operating Certificate Number', 'Facility ID', 'Facility Name', 'Age Group', 'Zip Code - 3 digits', 'Gender', 'Race', 'Ethnicity', 'Length of Stay', 'Type of Admission', 'Patient Disposition', 'Discharge Year', 'CCS Diagnosis Code', 'CCS Diagnosis Description', 'CCS Procedure Code', 'CCS Procedure Description', 'APR DRG Code', 'APR DRG Description', 'APR MDC Code', 'APR MDC Description', 'APR Severity of Illness Code', 'APR Severity of Illness Description', 'APR Risk of Mortality', 'APR Medical Surgical Description', 'Payment Typology 1', 'Payment Typology 2', 'Payment Typology 3', 'Attending Provider License Number', 'Operating Provider License Number', 'Birth Weight', 'Abortion Edit Indicator', 'Emergency Department Indicator', 'Total Charges', 'Total Costs']));
            if i == 1:
                data_no_nan.append(data_raw[i].dropna(subset = ['Health Service Area', 'Hospital County', 'Operating Certificate Number', 'Facility Id', 'Facility Name', 'Age Group', 'Zip Code - 3 digits', 'Gender', 'Race', 'Ethnicity', 'Length of Stay', 'Type of Admission', 'Patient Disposition', 'Discharge Year', 'CCS Diagnosis Code', 'CCS Diagnosis Description', 'CCS Procedure Code', 'CCS Procedure Description', 'APR DRG Code', 'APR DRG Description', 'APR MDC Code', 'APR MDC Description', 'APR Severity of Illness Code', 'APR Severity of Illness Description', 'APR Risk of Mortality', 'APR Medical Surgical Description', 'Payment Typology 1', 'Payment Typology 2', 'Payment Typology 3', 'Attending Provider License Number', 'Operating Provider License Number', 'Birth Weight', 'Abortion Edit Indicator', 'Emergency Department Indicator', 'Total Charges', 'Total Costs']));
            if i == 2:
                data_no_nan.append(data_raw[i].dropna(subset = ['Health Service Area', 'Hospital County', 'Operating Certificate Number', 'Facility Id', 'Facility Name', 'Age Group', 'Zip Code - 3 digits', 'Gender', 'Race', 'Ethnicity', 'Length of Stay', 'Type of Admission', 'Patient Disposition', 'Discharge Year', 'CCS Diagnosis Code', 'CCS Diagnosis Description', 'CCS Procedure Code', 'CCS Procedure Description', 'APR DRG Code', 'APR DRG Description', 'APR MDC Code', 'APR MDC Description', 'APR Severity of Illness Code', 'APR Severity of Illness Description', 'APR Risk of Mortality', 'APR Medical Surgical Description', 'Payment Typology 1', 'Payment Typology 2', 'Payment Typology 3', 'Attending Provider License Number', 'Operating Provider License Number', 'Birth Weight', 'Abortion Edit Indicator', 'Emergency Department Indicator', 'Total Charges', 'Total Costs', 'Ratio of Total Costs to Total Charges']));
        
        rows = 0
        columns = 0
        for i in range(len(data_no_nan)):
            rows = rows + len(data_no_nan[i].index)
            columns = columns + len(data_no_nan[i].columns)
    
    elif data_structure == 'list(csv)':
        row_index_tbr = []  #tbr stands for to be removed
        for row_index, row in enumerate(data_raw):
            if row_index == 0: #skip row with column names
                continue
            for cell_index, cell in enumerate(data_raw):
                if cell == "":
                    print(row)
                    row_index_tbr.append(data_raw)
                    break   
        for row_index, row in enumerate(data_raw):
            if row_index in row_index_tbr: #skip rows to be removed (tbr)
                continue
            data_no_nan.append(row)
        rows = len(data_no_nan)
        columns = len(data_no_nan[0])
        
    print("I have removed all the missing values in your data.")
    print("You now have %d inpatient discharges and %d that document these observations." % (rows, columns))
    return data_no_nan

def remove_outliers(data_no_nan,data_structure):
    '''
    # this function aims to deal with missing value
    # @param: data_raw is the original data including three years data 
    '''
    input(">: ")
    print("Right...would you like to remove data outliers?")
    input(">: ")
    if data_structure == 'dataframe(pandas)':
        col_names = ["Length of Stay","Total Charges","Total Costs"]
        pd.options.mode.chained_assignment = None
        for i in range(len(data_no_nan)):
            data_no_nan[i].loc[:,('Length of Stay')] = data_no_nan[i].loc[:,('Length of Stay')].apply(lambda x: pd.to_numeric(x, errors = 'coerce'))
            data_no_nan[i] = data_no_nan[i].dropna(subset = ['Length of Stay'])
            for j in range(len(col_names)):
                q1 = data_no_nan[i][col_names[j]].quantile(0.25)
                q3 = data_no_nan[i][col_names[j]].quantile(0.75)
                iqr = q3-q1 #Interquartile range
                fence_low  = q1-1.5*iqr
                fence_high = q3+1.5*iqr
                data_no_nan[i] = data_no_nan[i].loc[(data_no_nan[i][col_names[j]] > fence_low) & (data_no_nan[i][col_names[j]] < fence_high)]
        
        rows = 0
        columns = 0
        for i in range(len(data_no_nan)):
            rows = rows + len(data_no_nan[i].index)
            columns = columns + len(data_no_nan[i].columns) 
            
    elif data_structure == 'list(csv)':
        index_len_of_stay = data_no_nan[0].index('Length of Stay')
        index_total_charges = data_no_nan[0].index('Total Charges')
        index_total_costs = data_no_nan[0].index('Total Costs')
        my_list = [index_len_of_stay,index_total_charges, index_total_costs]  
        for i in my_list:
            for row in data_no_nan:
                new_temp = sorted(row[i])
                q1 = int(row[len(new_temp) * 0.25] - 1)
                q3 = int(row[len(new_temp) * 0.25] - 1)
                iqr = q3-q1 #Interquartile range
                fence_low  = q1-1.5*iqr
                fence_high = q3+1.5*iqr
                if row[i] < fence_low or row[i] > fence_high:
                    contine
                data_no_nan.append(row)         
            
    print("I have removed all outliers in your data.")
    print("You now have %d inpatient discharges and %d variables that document these observations." % (rows, columns))
    
    return data_no_nan

def data_align(data_no_nan_outlier, output_path):
    input(">: ")
    print("I am afraid this is not the best way to move forward. The variable names in your data are not consistent overtime.")
    print("Let me put these in a table for you. Please see below:")
    
    column_names = []
    for i in range(len(data_no_nan_outlier)):
        column_names.append(list(data_no_nan_outlier[i].columns))
    
    t = PrettyTable(['Year', 'Variable Names'])
    t.align['Variable Names'] = "l"
    for i in range(len(column_names)):
        t.add_row([2014+i, column_names[i]])
    print(t)
    
    input(">: ")
    
    print("Sure thing! I will use a dictionary for this. Processing...")
    #add columns
    data_no_nan_outlier[0]["new"] = data_no_nan_outlier[0]["Total Costs"]/data_no_nan_outlier[0]["Total Charges"]
    data_no_nan_outlier[1]["new"] = data_no_nan_outlier[1]["Total Costs"]/data_no_nan_outlier[1]["Total Charges"]
    for i in range(len(data_no_nan_outlier) - 1):
        data_no_nan_outlier[i].columns = data_no_nan_outlier[-1].columns
    
    print("Variable names match those in year 2016 now. Please see below:")
    column_names = []
    for i in range(len(data_no_nan_outlier)):
        column_names.append(list(data_no_nan_outlier[i].columns))
    
    t = PrettyTable(['Year', 'Variable Names'])
    t.align['Variable Names'] = "l"
    for i in range(len(column_names)):
        t.add_row([2014+i, column_names[i]])
    print(t)
    
    input(">: ")
    print("Yes, unless you want to do more data cleaning")
    input(">: ")
    
    for i in range(len(data_no_nan_outlier)):
        data_no_nan_outlier[i].to_csv(os.path.join(output_path, 'SPARCS' + str(2014+i) + '_clean' + '.csv'))