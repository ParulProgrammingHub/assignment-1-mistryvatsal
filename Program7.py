# WPP TO TAKE INPUT TWO NUMBERS X AS BASE AND Y AS POWER AND PRINT X^Y

angle1 = int(input('ENTER THE FIRST ANGLE :'))
angle2 = int(input('ENTER THE SECOND ANGLE :'))

def thirdangle(angle1, angle2):
    angle3 = 180 - angle1 - angle2
    return angle3

print('THIRD ANGLE IS ', thirdangle(angle1,angle2))
