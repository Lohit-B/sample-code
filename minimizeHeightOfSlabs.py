
#minimize hight of slabs while distributing 

def merge(a, b):
	sorted_arr = []
	j =0
	i = 0
	while(i < len(a) or j<len(b)):
		if (i == len(a)) :
			return sorted_arr + b[j:]
		if (j == len(b)):
			return sorted_arr + a[i:]
		if(a[i] < b[j]):
			sorted_arr.append(a[i])
			i += 1
		else :
			sorted_arr.append(b[j])
			j += 1
	return sorted_arr

def sort(arr):
	if len(arr) <= 1:
		return arr
	return merge(sort(arr[:len(arr)/2]), sort(arr[len(arr)/2:]))

class Block():
	def __init__(self):
		self.height = 0;
		self.slabs = []
	
	def _add(self, slab):
		self.slabs.append(slab)
		self.slabs = sort(self.slabs)
		self.height += slab
	
	def _remove(self, slab = None):
		if slab == None:
			x = self.slabs.pop()
		else:
			self.slabs.remove(slab)
			x = slab
		self.height -= x
		return x
		

def distribute(slabs, num_block):
	blocks =[Block() for i in range(num_block)]
	blocks[0].height = sum(slabs)
	blocks[0].slabs = sort(slabs)
	prime = blocks[0]
	iteration = 0

	while(True):
		if(len(prime.slabs) <= 1):
			return blocks
		iteration += 1
		for block in blocks[1:]:
			if (not prime.slabs):	return blocks
			block._add(prime._remove())
			if (block.height >= prime.height and iteration > 1):
				return blocks
	return blocks

def getNearestDiff(minB, maxB, limit):
	slabFromMin = None
	slabFromMax = None
	maxVariance = 0
	for slabMax in maxB.slabs: # slab in increasing orderi
		iteration  = 0
		for slabMin in minB.slabs:  #block slabs in decreasing order
			variance = slabMax - slabMin
			if(variance > limit):
				break
			if variance >= maxVariance: 
				maxVariance = variance
				slabFromMin = slabMin
				slabFromMax = slabMax
			iteration +=1
		if iteration == 0 :
			break
	return slabFromMin, slabFromMax

def getNearestSlab(block, limit): # block slabs in increasing order
	slabSelected = None
	diff = None
	for slab in block.slabs:
		if(slab >= limit):
			return slabSelected
		if diff is None:
			diff = abs(slab-limit)
			slabSelected = slab
		elif diff > abs(slab-limit):
			diff = abs(slab-limit)
			slabSelected = slab			
	return slabSelected

def level_max_min(maxB, minB):
	dif = maxB.height - minB.height
	slabExcMin, slabExcMax = getNearestDiff(minB, maxB, dif/2)
	slabToMove = getNearestSlab(maxB, dif)
	if(slabExcMax is None and slabToMove is None): return False
	if(slabExcMin is None):
		maxB._remove(slabToMove)
		minB._add(slabToMove)
		return True
	if(slabExcMax - slabExcMin > slabToMove):
		maxB._remove(slabExcMax)
		maxB._add(slabExcMin)
		minB._remove(slabExcMin)
		minB._add(slabExcMax)
	else:
		maxB._remove(slabToMove)
		minB._add(slabToMove)
	return True

def sortBlocks(block):
	return block.height

def shuffle(blocks):
	blocks = sorted(blocks, key=sortBlocks)
	print [block.slabs for block in blocks]
	if (len(blocks[-1].slabs) == 1): return blocks[-1].height
	if (blocks[-1].height == blocks[0].height) : return blocks[-1].height
	for block in blocks[:-1]:
		if (level_max_min(blocks[-1], block)):
			return shuffle(blocks)
	return blocks[-1].height

noOfBlocks = 5
height_slabs = [37, 31, 65, 38]

blocks = distribute(height_slabs, noOfBlocks)
print shuffle(blocks)
