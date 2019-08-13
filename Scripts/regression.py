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
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import pandas as pd

'''
# The regression.py script holds mainly for doing linear regression
'''


def reg_charge_cost(data_concat):
    '''
    # this function do the regression to investigate the relationship between the total charges and total costs
    # sets output path depending on the OS
    # @param: none
    '''
   
    input(">: ")
    print("Sure, let's explore the relationship between the total charges and total costs. \nWe randomly selected 2000 data points as a sample. 2500 of the sample data points are selected as training data sets and the rest are test sets")
    #used for initializing the internal random number generator, which will decide the splitting of data into train and test indices
    data_sample = data_concat.sample(n = 3000, random_state=1)
    
    X = data_sample['Total Charges']
    Y = data_sample['Total Costs']

    X=X.values.reshape(len(X.index),1)
    Y=Y.values.reshape(len(Y.index),1)
    
    # Split the data into training/testing sets
    X_train = X[:-500]
    X_test = X[-500:]

    # Split the targets into training/testing sets
    Y_train = Y[:-500]
    Y_test = Y[-500:]

# Plot outputs
    plt.scatter(X_test, Y_test,  color='black', alpha=0.3)
    plt.title('Test Data')
    plt.xlabel('Total Charges')
    plt.ylabel('Total Costs')

    plt.show()
    
    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(X_train, Y_train)

    # Plot outputs
    plt.plot(X_test, regr.predict(X_test), color='red',linewidth=3)
    plt.scatter(X_test, Y_test,  color='black', alpha=0.3)
    plt.title('Linear Regression')
    plt.xlabel('Total Charges')
    plt.ylabel('Total Costs')
    plt.show()