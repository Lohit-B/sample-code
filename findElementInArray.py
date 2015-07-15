import sys
from getopt import getopt, GetoptError

class node:
	def __init__(self, left, right, data, i, j):
		self.l = left
		self.r = right
		self.d = data
		self.i = i
		self.j = j

def createTree(data, i, j):
	if (len(data) == 1):
		return  node(None, None, data, i, j)
	else:
		return node(createTree(data[0 : len(data)/2], i, (i+j)/2), createTree(data[len(data)/2: len(data)], (i+j)/2+1, j), data, i, j)


def pprint(root):
	if root != None:
		print root.i, root.j, root.d
		pprint(root.l)
		pprint(root.r)
#	else:
#		print "NOT FOUND"

def findIndex(root, i, j):
	if root.l != None and root.l.i <= i and root.l.j >= j:
		return findIndex(root.l, i, j)
	elif root.r != None and root.r.i <= i and root.r.j >= j:
		return findIndex(root.r, i , j)
	elif root != None and root.i <= i and root.j >= j:
		return root
	else:
		return None
				
def main(argv):
	try:
		opts, args = getopt(argv, "hi:j:d:", ["start=", "end=", 'data='])
	except GetOptError:
		print "missing arg"
		sys.exit()
	for opt, arg in opts:
		if (opt == "-h"):
			print "a.py -i<int> -j<int> -d [data]" , "\nplease specify index range and array of data"
			sys.exit()
		elif (opt == "-i" or opt =="--start"):
			i = int(arg)
		elif (opt == "-j" or opt == '--end'):
			j = int(arg)
		elif (opt == '-d' or opt == '--data'):
			data = eval(arg)
	
	root = createTree(data, 1, len(data))
	node = findIndex(root, i, j)
	print node.d[i-node.i:j+1-node.i]

if __name__ == '__main__':
	 main(sys.argv[1:])

