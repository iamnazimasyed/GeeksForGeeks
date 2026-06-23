import math
class Solution:
    def switchCase(self, choice, arr):
        # Code here
        if choice == 1:
            r = arr[0]
            return math.pi * r * r
        elif choice == 2:
            l = arr[0]
            b = arr[1]
            return l * b
        