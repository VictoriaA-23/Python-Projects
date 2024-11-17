#This program determines the relative position of point p2 based on the
##given line from point p0 to point p1

#allows user to enter the coordinates of points p0, p1, and p2
point_0x = float(input('Enter the x-coordinate for point p0: '))
point_0y = float(input('Enter the y-coordinate for point p0: '))

point_1x = float(input('Enter the x-coordinate for point p1: '))
point_1y = float(input('Enter the y-coordinate for point p1: '))

point_2x = float(input('Enter the x-coordinate for point p2: '))
point_2y = float(input('Enter the y-coordinate for point p2: '))


#uses the equation to determine the position of point p2
#if the answer is > 0 then p2 is to the left of the line
if (point_1x - point_0y) * (point_2y - point_0y) - (point_2x - point_0x) * (point_1y - point_0y) > 0:
    print('p2 at coordinates', (point_2x , point_2y), 'is on the left side of the line\nfrom point', (point_0x , point_0y), 'to point', (point_1x , point_1y))

#if the answer is < 0 then p2 is to the right of the line
elif (point_1x - point_0y) * (point_2y - point_0y) - (point_2x - point_0x) * (point_1y - point_0y) < 0:
    print('p2 at coordinates', (point_2x , point_2y), 'is on the right side of the line\nfrom point', (point_0x , point_0y), 'to point', (point_1x , point_1y))

#if the answer is = 0 then p2 is on the line
else:
        print('p2 at coordinates', (point_2x , point_2y), 'is on the line\nfrom point', (point_0x , point_0y), 'to point', (point_1x , point_1y))


