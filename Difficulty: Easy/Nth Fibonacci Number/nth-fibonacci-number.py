class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        a = 0
        b = 1
        for i in range(n):
            a, b =b, a + b
        return a