import math
print ('This program calculates the area and circumfrence of a circle with a given radius')
r = float(input("please enter the circle's radius: "))
print ('You entered', r, '. Calculating now...')
area = math.pi * (r**2)
circumfrence = 2 * math.pi * r
print ('The area of the circle is ', area, 'and the circumfrence of the circle is ', circumfrence, '.')
