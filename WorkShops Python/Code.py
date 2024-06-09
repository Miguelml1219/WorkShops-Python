print('Value of the First leg in:')
x1 = float(input('X\u2081: '))
y1 = float(input('Y\u2081: '))

print('Value of the Second leg in:')
x2 = float(input('X\u2082: '))
y2 = float(input('Y\u2082: '))

print('Value of the Third leg in:')
x3 = float(input('X\u2083: '))
y3 = float(input('Y\u2083: '))

Acx = x2- x1
Acy = y2 - y1
Bcx = x3 - x2
Bcy = y3 - y2
Ccx = x3- x1
Ccy= y3 - y1

A = ((Acx)**2 + (Acy)**2)**0.5
B = ((Bcx)**2 + (Bcy) **2)**0.5
C = ((Ccx)**2 + (Ccy) **2)**0.5
print('')
S = (A + B + C) / 2
print('The Semi-Perimeter is: ',round (S,3))
At = (S*(S-A)*(S-B)*(S-C))**0.5
print('The Area of the Triangle is: ',round (At,3))
