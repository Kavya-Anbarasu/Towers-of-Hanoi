x = [0]
def hanoi(height, first, end, middle):
	if height == 1:
		print ("Move from %s to %s") %(first, end)
		x[0] += 1
	else:	
		hanoi(height - 1, first, middle, end)
		print ("Move from %s to %s") %(first, end)
		x[0] += 1
		hanoi(height - 1, middle, end, first)
	return(x[0])

hanoi(5 , "A" , "B" , "C")
print(x[0])