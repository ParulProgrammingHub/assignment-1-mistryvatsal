# Write a program to calculate Compound Interest.

def compound_interest(principal,time,rate):
    x=(1+(rate/100))**time
    interest_value=(principal*x-principal)
    return interest_value
print('The Compound Interest Value is : ',compound_interest(int(input('Enter The Principal Amount : ')),int(input('Enter Time In Years : ')),float(input('Enter The Interest Percentage : '))))
