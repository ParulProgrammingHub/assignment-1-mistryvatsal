# WPP TO TAKE INPUT AS MARKS OF 5 SUBJECTS, CALCULATE THE MEAN AND PRINT PERCENTAGE , MEAN, PASS IF GREATER THAN 35.

s = input('ENTER THE MARKS OF 5 SUBJECTS SEPARATED EACH BY COMMA : ')
marks = s.split()
print(marks)
some = sum(int(marks))
print(some)

'''
marks = list(map(int, s.split()))
mean = sum(marks) / float(len(marks))
percent = mean * 100
if percent < 35:
    print('YOU HAVE FAILED')
    print('PERCENT : ', percent)
print('YOU HAVE PASSED')
print('PERCENT : ', percent)
'''

