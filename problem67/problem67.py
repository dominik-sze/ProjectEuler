class Problem68:
	def __init__(self):
		self.__triangle = []
		self.__loadArrayFromFile()

	def __loadArrayFromFile(self, filename = 'triangle.txt'):
		try:
			with open(filename, 'r') as fp:
				for line in fp:
					self.__triangle.append([int(v) for v in line.split(' ')])
		except IOError as e:
			print('I/O error ({}): {}'.format(e.errno, e.strerror))

	def solution(self):
		for i in range(len(self.__triangle)-2, -1, -1):
			for j, v in enumerate(self.__triangle[i]):
				self.__triangle[i][j] = max(self.__triangle[i][j]+self.__triangle[i+1][j],self.__triangle[i][j]+self.__triangle[i+1][j+1]) 

		print(self.__triangle[0][0])	

if __name__=='__main__':
	p = Problem68()
	p.solution()
