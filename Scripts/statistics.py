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
import os
import matplotlib.pyplot as plt
from tabulate import tabulate

'''
# The statistic.py script holds mainly for data visualization
'''

def import_clean_data(output_path):
    '''
    # this function aims to get the final data which is cleaned
    #@parameter: the output_path is the output address where we can output the data being cleaned
    '''
    data_clean = []
    for i in range(3):
        df = pd.read_csv(os.path.join(output_path, 'SPARCS' + str(2014+i) + '_clean' + '.csv'), index_col = None, header = 0, low_memory = False)
        data_clean.append(df)
    return data_clean

def plot_asthma(data_clean):
    '''
     # this function aims to draw a bar chart to get the Frequency count of patients with asthma conditions by year and type of admission'
    #@parameter: the cleaning data
    '''
    print("Sure thing! I can plot some graphs for you. What do you want to know more precisely?")
    input(">: ")
    print("This is a very interesting question. Let me prepare some graphs for you...")
    print("Here is what I found:")
    
    data_asthma = []
    for i in range(len(data_clean)):
        data_asthma.append(data_clean[i].loc[data_clean[i]['CCS Diagnosis Description'] == 'Asthma'])
    
    global asthma_concat
    asthma_concat = pd.concat(data_asthma, axis=0, ignore_index=True)
    
    asthma_count = asthma_concat.groupby(['Type of Admission','Discharge Year']).size()

    count_plot = asthma_count.Emergency.plot(kind = 'bar', color = 'red', title = 'Frequency count of patients with asthma conditions \n by year and type of admission', label = 'Emergency')
    count_plot = asthma_count.Urgent.plot(kind = 'bar', bottom = asthma_count.Emergency,color = 'blue', label = 'Urgent')
    count_plot.set_xlabel('Discharge Year')
    count_plot.set_ylabel('Frequency Count')
    plt.xticks(rotation = 0)
    plt.legend()
    plt.show()

def plot_pay_source():
    '''
     # this function aims to draw a pie to investigate the proportion of different type of payment sources for patients'
    #@parameter: the cleaning data
    '''
    input('>: ')
    print("Indeed, very interesting. Would you like me to plot some more graphs?")
    input(">: ")
    print("It seems that there are 10 types of payment sources. I think a pie chart is more appropriate here. Do you agree?")
    input(">: ")
    print("Interesting results again. Please see below what I found in the data:")
    
    plt.figure(figsize=(6,7.5))
    pay_source_plot = asthma_concat.groupby(['Payment Typology 1']).size().plot(kind = 'pie', title = 'Type of payment sources for patients with asthma conditions', shadow = True, labeldistance = None, radius = 1.1)
    plt.legend(bbox_to_anchor=(0, 0), loc = "upper left", ncol=2)
    plt.show()
    
#below here is my findings
def print_stay_length_by_disease(data_clean):
    '''
    # this function draw a table to investigate the  average length of stay under different severities of illness. 
    #The data has been sorted by length of stay from shortest to longest:"
    '''
    input(">: ")
    print("In the following is the average length of stay under different severities of illness. \nThe data has been sorted by legnth of stay from shortest to longest:")
    global data_concat
    data_concat = pd.concat(data_clean, axis=0, ignore_index=True) 
    stay_disease = data_concat.groupby('APR Severity of Illness Description', as_index=False)['Length of Stay'].mean().sort_values('Length of Stay')
    print(tabulate(stay_disease, headers='keys', tablefmt='psql'))
    print("As the illness is more severe, the length of stay is longer.")
    return data_concat

def plot_cost_vs_year():
    '''
    # this function aims to plot a line chart to investigate changes of average total costs in different years. 
    '''
    input(">: ")
    print("In the following is the changes of average total costs in different years:")
    cost_year = data_concat.groupby('Discharge Year', as_index=False)['Total Costs'].mean().sort_values('Discharge Year')
    cost_year_plot = cost_year.plot(x = 'Discharge Year', y = 'Total Costs')
    axes = plt.gca()
    axes.set_xlim([2013.5,2016.5])
    axes.set_ylim([9600,11800])
    plt.xticks([2014, 2015, 2016])
    plt.show()
    print("The average total cost increases year by year")
    
def plot_charge_cost():
    '''
    # this function aims to plot a scatter to investigate relationship between total charges and total cost. 
    '''
    input(">: ")
    print("I randomly selected 1000 rows of data as the sample. In the following is the scater plot between total charges and total cost")
    data_sample = data_concat.sample(n = 1000, random_state=1)
    charge_cost = data_sample.plot.scatter(x='Total Charges', y='Total Costs', color='DarkBlue')
    plt.show()
    print("Total charges and total cost is more or less in linear relationship. When the total charges is larger, the data distribution is more random.")