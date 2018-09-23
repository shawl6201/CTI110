#Determine the projected profit amount based on total sales
#September 12, 2018
#CTI-110P2T1-Sales Prediction
#Leslie Shaw

#Get the projected total sales
total_sales = float(input('Enter the projected sales: '))

#Calculate the profit as 23 percent of total sales
profit = total_sales * 0.23

#Display the profit
print('The profit is $', format(profit,',.2f'))
                    
