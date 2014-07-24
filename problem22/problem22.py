#file sorted using vim
#commands used:
#  :%s/,/\r/g
#  :%s/"//g
#  :sort

def problem22():
	SUM = 0
	try:
		with open('names.txt','r') as fp:
			for i, line in enumerate(fp):
				sum = 0
				for c in line.rstrip():
					sum+=(ord(c)-64)
				sum*=(i+1)
				SUM+=sum
	except IOError as e:
		print('I/O error ({}):'.format(e.errno, e.strerror))
	print(SUM)

if __name__=='__main__':
	problem22()
