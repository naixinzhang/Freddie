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

import os
import platform

def operating_system(OS):
    '''
    # this function sets the drive letter depending on the specified OS
    # @param: OS
    '''
    if OS == platform.system():
        global drive_letter 
        drive_letter = os.path.splitdrive(os.getcwd())[0]
        drive_letter = os.path.join(drive_letter, os.sep)
        print("Nice. Your drive letter is now set to %s" % drive_letter)
        return True
    else:
        print("Wrong operating system")
        return False
    
def input_path(path):
    '''
    # this function sets the input path
    # @param: path
    ''' 
    path_list = path.split(",")
    input_path_curr = ""
    for i in range(len(path_list)):
        input_path_curr = os.path.join(input_path_curr,path_list[i])
    return input_path_curr

def output_path(path):
    '''
    # this function sets the output path
    # @param: path
    '''
    path_list = path.split(",")
    output_path_curr = ""
    for i in range(len(path_list)):
        output_path_curr = os.path.join(output_path_curr,path_list[i])
    return output_path_curr        
        
def input_path_conversation():
    '''
    # this function takes input path info provided by user 
    # sets output path depending on the OS
    # @param: none
    '''
    global input_path_final
    input_path_final = ""
    input_path_curr = ""
    
    while not os.path.isdir(input_path_final):
        if len(input_path_final) > 0:
            print("Wrong path")
        print("What is your input path?")
        input_path_info = input(">: ")
        input_path_curr = input_path(input_path_info)
        input_path_final = os.path.join(drive_letter, input_path_curr)
    print('Your input path is now set to',input_path_curr)
    
    return input_path_final
 
def output_path_conversation():
    '''
    # this function takes output path info provided by user
    # sets output path depending on the OS
    # @param: none
    '''
    global output_path_final
    output_path_final = ""
    output_path_curr = ""
    
    while not os.path.isdir(output_path_final):
        if len(output_path_final) > 0:
            print("Wrong path")
        print("What is your output path?")
        output_path_info = input(">: ")
        output_path_curr = output_path(output_path_info)
        output_path_final = os.path.join(drive_letter, output_path_curr)
    print('Your output path is now set to',output_path_curr)
    
    return output_path_final