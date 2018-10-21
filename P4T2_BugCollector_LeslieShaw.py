#This program was created to calculate
#the amount of bugs a person has collected
#within 5 days
#October 18, 2018
#CTI-110 P4T2 - Bug Collector
#Leslie Shaw

def main():
    
    #Initialize the accumulator.
    total= 0

    #Get bugs collected for each day.
    for day in range (1, 6):
            #User will be asked to input information.
            print('Please enter bugs collected on day', day)

            #Input the number of bugs.
            bugs= int(input())

            #Add total of bugs.
            total += bugs

    #Display the total bugs.
    print('You have collected a total of', total, 'bugs')
    
main ()
