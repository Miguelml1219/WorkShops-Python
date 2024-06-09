x=[]
y=[]
xN=[]
yN=[]
def readCoordinate(n):
    v = 1
    for i in range (n):
        ord = float(input(f'Enter the coordinate X{v}: '))
        abs = float(input(f'Enter the coordinate Y{v}: '))
        print('')
        x.append(ord)
        y.append(abs)
        v = v + 1
def readnumber(w):
     for i in range (w):
        m=float(input('Enter a number: '))
        xN.append(m)
        r = 4.0*m - 11
        yN.append(r)
     
def calculateSlope(x1,y1,x2,y2):
     return ((y2-y1)/(x2-x1))

def calculateDistance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)

def calculateB(x1,y1,slope):
    return y1 - slope * x1
    
n = int(input('Points to read: '))
readCoordinate(n)
print('Numbers of the list X: ',x)
print('Numbers of the list Y: ' ,y)
print('')
distance=calculateDistance(x[0],y[0],x[1],y[1])
distance1=calculateDistance(x[1],y[1],x[2],y[2])
distance2=calculateDistance(x[0],y[0],x[2],y[2])

if distance + distance1 > distance2 and distance1 + distance2 > distance and distance2 + distance > distance1:
        print('The values entered form a triangle')
        print('')
        slope=calculateSlope(x[0],y[0],x[1],y[1])
        slope1=calculateSlope(x[1],y[1],x[2],y[2])
        slope2=calculateSlope(x[0],y[0],x[2],y[2])

        B=calculateB(x[0],y[0],slope)
        B1=calculateB(x[1],y[1],slope1)
        B2=calculateB(x[2],y[2],slope2)

        print(('Distance of coordinate 1 is: '),round(distance,2))
        print(('Distance of coordinate 2 is: '),round(distance1,2))
        print(('Distance of coordinate 3 is: '),round(distance2,2))
        print('')
        print(('Slope of coordinate 1 is: '),round(slope,2))
        print(('Slope of coordinate 2 is: '),round(slope1,2))
        print(('Slope of coordinate 3 is: '),round(slope2,2))
        print('')
        print(('B of coordinate 1 is: '),round(B,2))
        print(('B of coordinate 2 is: '),round(B1,2))
        print(('B of coordinate 3 is: '),round(B2,2))
        print('')
        print(('Ecuation of the coordinate 1 is: y ='),round(slope,2),(' x + '),round(B,2))
        print(('Ecuation of the coordinate 2 is: y ='),round(slope1,2),(' x + '),round(B1,2))
        print(('Ecuation of the coordinate 2 is: y ='),round(slope2,2),(' x + '),round(B2,2))
        
        w= int(input('Enter number of times for tabulation: '))
        readnumber(w)
        print('Numbers of the list X: ',xN)
        print('Numbers of the list Y: ' ,yN)  
else:
    print('The values entered do not form a triangle')



