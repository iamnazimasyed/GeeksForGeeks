class Solution:
	def countOddEven(self, arr):
		#Code here
		countOdd = 0
		countEven = 0
		for num in arr:
		    if num % 2 == 0:
		        countEven += 1
		    else:
		        countOdd += 1
		return countOdd, countEven