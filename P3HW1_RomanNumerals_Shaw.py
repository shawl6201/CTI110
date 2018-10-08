# CTI-110 
# P3HW1 - Roman Numerals 
# Leslie Shaw
# October 7, 2018
#This program will show the Roman numeral for whole numbers 1 through 10.
#Anything less than 1 or greater than 10 will display an error message.

def main():
    #Input a number 1 through 10
    number=int(input('Enter a number 1 through 10:'))

    #Variables for roman numerals 1 through 10
    Roman1='I'
    Roman2='II'
    Roman3='III'
    Roman4='IV'
    Roman5='V'
    Roman6='VI'
    Roman7='VII'
    Roman8='VIII'
    Roman9='IX'
    Roman10='X'

    #Determine the Roman numeral
    if number==1:
        print('The Roman numeral for 1 is:', Roman1)
    else:
        if number==2:
            print('The Roman numeral for 2 is:',Roman2)
        else:
            if number==3:
                print('The Roman numeral for 3 is:',Roman3)
            else:
                if number==4:
                    print('The Roman numeral for 4 is:',Roman4)
                else:
                    if number==5:
                        print('The Roman numeral for 5 is:',Roman5)
                    else:
                        if number==6:
                            print('The Roman numeral for 6 is:',Roman6)
                        else:
                            if number==7:
                                print('The Roman numeral for 7 is:',Roman7)
                            else:
                                if number==8:
                                    print('The Roman numeral for 8 is:',Roman8)
                                else:
                                    if number==9:
                                        print('The Roman numeral for 9 is:',Roman9)
                                    else:
                                        if number==10:
                                            print('The Roman numeral for 10 is:',Roman10)
                                        else:
                                            print ('Unknown. Item entered was not a number 1 through 10')

main()
