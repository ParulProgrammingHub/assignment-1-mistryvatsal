# WPP TO ENTER DAYS AND CONVERT INTO YEARS,MONTHS AND DAYS AND PRINT.

days = int(input('ENTER THE DAYS : '))
months = days / 30
days = days % 30
years = months / 12
if years is not 0:
    months = months % 12
print('YEARS : ',int(years), 'MONTHS : ',int(months),'DAYS : ',int(days))
