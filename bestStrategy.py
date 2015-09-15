weights = [1,9,3,34,45,78,90,100]

def bestStrategy(weights, tot_weight, printStatement):
#	print printStatement, weights, tot_weight
	if len(weights) == 1 :
		print printStatement+'0', tot_weight + weight[0]
		return tot_weight + weight[0]
	elif len(weights) == 2:
		print printStatement+("01" if weights[0]>weights[1] else "10"), tot_weight + max(weights)
		return tot_weight + max(weights)

	
	return max(bestStrategy(weights[1:-1], tot_weight + weights[0], printStatement+'0-1,'), bestStrategy(weights[1:-1], tot_weight + weights[-1], printStatement+"-10,"), bestStrategy(weights[:-2], tot_weight + weights[-1], printStatement+"-1-2,"), bestStrategy(weights[2:], tot_weight + weights[0], printStatement+"01,"))

print bestStrategy(weights, 0, "Start")
