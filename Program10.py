# Write a program to calculate Simple Interest.

principle_amount = float(input('ENTER THE PRINCIPLE AMOUNT : '))
time = int(input('ENTER TIME PERIOD IN YEARS : '))
roi = float(input('ENTER RATE OF INTEREST : '))
print('SIMPLE INTEREST IS : ', (principle_amount * time * roi) / 100)
