# CTI-110 
# P3HW2 - Shipping Charges 
# Leslie Shaw
# October 6, 2018

def main():
    #This program is to determine how much a person will pay in shipping based on
    #the weight of their package
    package_weight= float(input('Enter the weight of your package:'))

    #Calculate shipping costs
    shipping_cost1= package_weight*1.5
    shipping_cost2= package_weight*3
    shipping_cost3= package_weight*4
    shipping_cost4= package_weight*4.75

    #Determine the shipping cost
    if package_weight <=2:
        print('Your shipping cost is: $', format(shipping_cost1,',.2f'))
    else:
        if package_weight <=6:
            print('Your shipping cost is: $', format(shipping_cost2,',.2f'))
        else:
            if package_weight <=10:
                print('Your shipping cost is: $', format(shipping_cost3,',.2f'))
            else:
                print('Your shipping cost is: $', format(shipping_cost4,',.2f'))
main ()
