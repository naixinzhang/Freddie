################################# NY HOSPITALS #################################
#
# Title:
# Files: paths.py, datacleaning.py, inputdata.py, [add more here]
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


#import modules here
from Scripts import hospitalsNY as hp
from Scripts import path
from Scripts import input as ip
from Scripts import cleaning as cl


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
        input_data_structure = input(">: ")
        state, data = ip.read_data(input_names, input_data_structure, input_path)
    return data
def data_cleaning(data_raw):
    '''
    # your comments here
    '''
    cl.row_col_number(data_raw)
    

def summary_stats():
    '''
    # your comments here
    '''
    pass 
    
def linear_model():
    '''
    # your comments here
    '''
    pass 
        

    
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
    data_raw = input_data()
    
    data_cleaning(data_raw)

if __name__ == "__main__":
    main()