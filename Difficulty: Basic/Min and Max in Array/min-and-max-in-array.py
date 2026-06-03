class Solution:
    def getMinMax(self, arr):
        # code here
        min = arr[0]
        max = arr[0]
        for num in arr:
            if num > max:
                max = num
            elif num < min:
                min = num
        return min, max