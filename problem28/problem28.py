def problem28():
	sum = 1
	counter = 1
	for j in range(3, 1002, 2):
		sum+=j*j
		sum+=(j*j - counter*2)
		sum+=(j*j - counter*4)
		sum+=(j*j - counter*6)
		counter+=1
	print(sum)

if __name__=='__main__':
	problem28()
