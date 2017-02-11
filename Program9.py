# WPP TO TAKE INPUT AS MARKS OF 5 SUBJECTS, CALCULATE THE MEAN AND PRINT PERCENTAGE , MEAN, PASS IF GREATER THAN 35.

s = input('Enter marks of 5 subjects out of 100 separated by whitespace each: ')
numbers = list(map(int, s.split()))
some = sum(numbers)
mean = sum(numbers) / len(numbers)
percent = mean
if percent < 35:
    print('YOU HAVE FAILED')
    print('PERCENT : ', percent)
print('YOU HAVE PASSED')
print('PERCENT : ', percent,'%')
