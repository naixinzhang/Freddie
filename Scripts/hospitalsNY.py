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