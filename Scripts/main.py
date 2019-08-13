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

#import modules here
import hospitalsNY as hp
import path
import input as ip
import cleaning as cl
import statistics as st
import regression as rg


'''
#
# The main.py script holds the user input and response formation for a data analyst 
# chatboot that collects user input and responds appropriately. 
#
'''

def os_and_drive_letter():
    '''
    # sets OS and drive letter. The user is prompted to enter the computer's
    # operating system. Example: Windows, Mac.
    # @param: none.
    ''' 
    state = False
    while state == False:
        print("What is your computer's operating system?")
        input_OS = input(">: ")
        state = path.operating_system(input_OS)

def input_path():
    '''
    # sets the input path and saves its value globally
    # The user is prompted to enter the input path.
    # For example, if user path is "N:\Classes\AAE875\DataAnalytics\FinalProgram\Input"
    # then Classes, AAE875, DataAnalytics, FinalProgram, Input will be entered
    # in the command line.
    # @param: none.
    '''
    global input_path
    input_path = path.input_path_conversation()
    
def output_path():
    '''
    # sets the output path and saves its value globally.
    # The user is prompted to enter the output path.
    # For example, if user path is "N:\Classes\AAE875\DataAnalytics\FinalProgram\Output"
    # then Classes, AAE875, DataAnalytics, FinalProgram, Output will be entered
    # in the command line.
    # @param: none.
    '''
    global output_path
    output_path = path.output_path_conversation()
    
def input_data():
    '''
    # inputs the raw data. The user is prompted to enter the name of the data
    # files (in csv format). For example: SPARCS2014.csv, SPARCS2015.csv,
    # SCARCS2016.csv
    # inputs the data structure. The user is prompted to enter the desired data
    # structure. Available options are: list(csv), array (numpy), dataframe(pandas)
    # @param: none
    '''
    state = False
    while state == False:
        print("What are the names of your data files?")
        input_names = input(">: ")
        print("What is the data structure you would like to work with?")
        global data_structure
        data_structure = input(">: ")
        state, data = ip.read_data(input_names, data_structure, input_path)
    return data

def data_cleaning(data_raw, output_path):
    '''
    # this function will get the current raw data's column number and row number
    # then remove mising values outlier values then make the column name consistent
    # @param: data_raw is the original data including three years data 
    #@and the output_path is the output address where we can outpu the data being cleaned
    '''
    cl.row_col_number(data_raw,data_structure)
    data_no_nan = cl.remove_missing_value(data_raw,data_structure)
    data_no_nan_outlier = cl.remove_outliers(data_no_nan)
    cl.data_align(data_no_nan_outlier, output_path)
def summary_stats():
    '''
    # this function includes using the final data to draw plots.I use five different formates to plot
    '''
    
    data_clean = st.import_clean_data(output_path)
    st.plot_asthma(data_clean)
    st.plot_pay_source()
    global data_concat
    data_concat = st.print_stay_length_by_disease(data_clean)
    st.plot_cost_vs_year()
    st.plot_charge_cost()
def linear_model():
    '''
    # this function doing the regression
    '''
    rg.reg_charge_cost(data_concat)
        

    
######## runs main script ########
##################################

def main():
    # print welcome prompts
    hp.welcome_prompt()

    # print greetings; get user name
    user_input = input(">: ")
    hp.greetings(user_input)
    
    # set OS and drive letter
    os_and_drive_letter()

    # set input path
    input_path()
    
    # set output path
    output_path()
    
    # input the data
    data_raw, data_structure = input_data()
    
    data_cleaning(data_raw,data_structure,output_path)
    
    summary_stats()
    linear_model()
if __name__ == "__main__":
    main()