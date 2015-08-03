class T:
	def __init__(this, l, r, v):
		this.l = l
		this.r = r
		this.v = v

def getDepth(root):
	if root != None:
		depthR = getDepth(root.r)
		depthL = getDepth(root.l)
		return depthR+1 if depthR > depthL else depthL+1
	else :
		return 0
	
def createTree(i, j):
	if i < 3 and  j < 7:
		return  T(createTree(i+1, j), createTree(i, j+1), str(i+j))
	return None

def printTree(root):
	if (root != None):
		print(root.v)
		printTree(root.l)
		printTree(root.r)
	
def extendLine(line, depth):
	diff = depth - len(line)
	for i in range(diff-1) :
		line = line + " "
	return line

def createLinesForNode(node, lineNumber, lineDepth, arrOfLine):
	arrOfLine[lineNumber] = extendLine(arrOfLine[lineNumber], lineDepth) + str(node.v)
	lineDepth = len(arrOfLine[lineNumber])
	#print len(arrOfLine[lineNumber]), (arrOfLine[lineNumber])
	
	nodeSym ='|'
	nodeUp = '|'
	nodeDown ='|'
	vert = '|'
	hor = '-'

	if (node.r is not None or node.l is not None):
		arrOfLine[lineNumber] = arrOfLine[lineNumber] + hor + nodeSym
		lineDepth = len(arrOfLine[lineNumber])

	if (node.l is not None):
		arrOfLine[lineNumber-1] =  extendLine(arrOfLine[lineNumber-1], lineDepth) + vert
		arrOfLine[lineNumber-2] = extendLine(arrOfLine[lineNumber-2], lineDepth) + vert + hor
		lineDepth = len(arrOfLine[lineNumber-2])
		arrOfLinei = createLinesForNode(node.l, lineNumber-2, lineDepth, arrOfLine)

	if (node.r is not None):
		arrOfLine[lineNumber + 1] =  extendLine(arrOfLine[lineNumber+1], lineDepth) + vert
		arrOfLine[lineNumber+2] =  extendLine(arrOfLine[lineNumber+2], lineDepth) + nodeDown + hor
		lineDepth = len(arrOfLine[lineNumber+2])
		arrOfLine = createLinesForNode(node.r, lineNumber+2, lineDepth, arrOfLine)


	return arrOfLine
		
def lineForm(t):
	noOfLines = getDepth(t)*6
	arrOfLines = ["" for i in range(noOfLines)]
	return  createLinesForNode(t, noOfLines/3, 0, arrOfLines)

def printLines(lines):
	for line in lines:
		if line is not "":
			print line+'\n'

if __name__== '__main__':
	ll = T(None, None, 11)
	lr = T(None, None, 12)
	rr = T(None, None, 22)
	rl = T(None, None, 21)
	r = T(rl, rr, 2)
	l = T(ll, lr, 1)
	t = T(l, r, "T")
	printTree(t)
	lines = lineForm(t)
	printLines(lines)

