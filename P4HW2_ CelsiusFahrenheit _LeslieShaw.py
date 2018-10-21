#This program converts 0-20 degrees Celsius
#to its Fahrenheit equivalent and displays it
#in a chart format.
# October 20, 2018
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# Leslie Shaw

def main():
    start_celsius=0                       #Start temperature
    end_celsius=21                        #End temperature
    increment=1                           #increments


    #print table headings
    print('Celsius\tFahrenheit')
    print('_________________')

    #print temperature
    for celsius in range(21):
        Fahrenheit= (1.8*celsius) + 32 
        print(celsius, '\t', format(Fahrenheit,',.1f'))
main()
