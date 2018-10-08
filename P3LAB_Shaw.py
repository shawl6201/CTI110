#This program will convert a numerical grade into a letter grade
#Shaw

def main():
    #This program will convert a numberical grade into a letter grade
    #The system uses a 10-point grading scale
    A_score=90
    B_score=80
    C_score=70
    D_score=60

    #Input a score
    score=int(input('Enter grade:'))

    #Determine the letter grade
    if score >= A_score:
        print ('Your grade is: A.')
    else:
        if score >=B_score:
            print ('Your grade is: B.')
        else:
            if score >=C_score:
                print ('Your grade is C.')
            else:
                if score >=D_score:
                    print ('Your grade is D.')
                else:
                    print ('Your grade is F.')
main ()
