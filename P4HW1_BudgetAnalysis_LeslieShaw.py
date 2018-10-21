#This program will create a running total of
#money spent and determine if the user is over
#or under their budget based on total expenses.
#October 19, 2018
#CTI-110 P4HW1 - Budget Analysis
#Budget Analysis
#Leslie Shaw

def main():
    #Create a variable for the budget
    max_budget= float(input('Please enter your budget for this month: $ '))

    #Set sentinel value
    leave= 0

    #set accumulator
    total=0.00

    #Prompt user to enter first expense
    #and continue if necessary
    print('Enter expense or press 0 to end.')
    expense= float(input('Expense: $ '))
    while expense != leave:
        total += expense
        expense= float(input('Expense: $ '))
    if total < max_budget:
        print('You were within your budget this month')
        print('with a total of $', format(total, ',.2f'))
    else:    
        print('You spent $', format(total, ',.2f'), 'which made you')
        print('go over your budget.')
main()
