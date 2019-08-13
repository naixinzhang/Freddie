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

'''
# The hospitalsNY.py script holds mainly for user input and response formation for greetings
'''

def welcome_prompt():
    '''
    # prints the welcome prompt.
    # @param: none.
    '''
    print("Hi, I'm Freddie, what is your name?")
    
def greetings(user_name):
    '''
    # Freddie gets the user name and asks what he can do.
    # @ param: user_name.
    '''
    print("Nice to meet you %s. How can I help you today?" % user_name)
    input_instructions = input(">: ")
    print("Ok, I can help you with this.")