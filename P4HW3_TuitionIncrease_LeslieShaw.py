#This program will demonstrate a tuition
#increase of 3% each year over the next
#five years.
#October 20, 2018
#CTI-110 P4HW3 - Tuition Increase
#Leslie Shaw


def main():

    #Create headings
    print('Year\tTuition')
    print('-----------------------')

    #Indicate starting tuition
    start_tuition= 8000

    for year in range(1,6):
        start_tuition += (.03 * start_tuition)
        print(year,'\t$', format(start_tuition, '.2f'))
main()
