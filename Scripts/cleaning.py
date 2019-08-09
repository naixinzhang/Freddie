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
# Persons: 
# Online sources:
#
############################### 80 COLUMNS WIDE ################################


def row_col_number(data_raw):
    print("Ok, good choice. Tell me what you would like to do next?")
    input(">: ")
    rows = 0
    columns = 0
    for i in range(len(data_raw)):
        rows = rows + len(data_raw[i].index)
        columns = columns + len(data_raw[i].columns)
    print("Let me check...oh...this data is really big!")
    print("You have %d inpatient discharges and %d variables that documnet these observations" % (rows, columns))

