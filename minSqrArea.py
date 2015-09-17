# given n number of points, calculate a square with min area which contains atleast k points

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		return self.x is other.x and self.y is other.y

def remove(x, y, k, val):
	toRemove = None
	print k,val
	if val is 'x':
		if(x[k-1].x- x[0].x > x[-1].x > x[-k].x):
			toRemove = x[0]
		else:
			toRemove = x[-1]
	if val is 'y':
		if(y[k-1].y- y[0].y > y[-1].y > y[-k].y):
			toRemove = y[0]
		else:
			toRemove = y[-1]
	
	x.remove(toRemove)
	y.remove(toRemove)
		

def calMinArea(x, y, k):
	removed = 0
	n = len(x)
	while removed <= n-k:
		if((x[-1].x-x[0].x) > (y[-1].y-y[0].y)):
			remove(x, y, k, 'x')
		elif(x[-1].x-x[0].x == y[-1].y-y[0].y):
			x0_K = x[k-1].x - x[0].x
			y0_K = y[k-1].y - y[0].y
			xn_k = x[-1].x - x[-k].x
			yn_k = y[-1].y - y[-k].y
			if (max(xn_k, x0_k) > max(yn_k, y0_k)):
				remove(x, y, k, 'x')
			else:
				remove(x, y, k, 'y')
		else:
				remove(x, y, k, 'y')
		removed += 1
	return (max(x[-1].x-x[0].x, y[-1].y-y[0].y))**2

arrP = [Point(1,3), Point(2,4), Point(-3,8), Point(8, 19), Point(3,9), Point(-10, 4), Point(0,0)]
sortedX = sorted(arrP, key = lambda point : point.x)
sortedY = sorted(arrP, key = lambda point : point.y)
print calMinArea(sortedX, sortedY, 3)				
