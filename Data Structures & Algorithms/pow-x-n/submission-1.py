class Solution:
    def split_pow(self, x,n):
        if n == 0:
            return 1
        if n == 1: 
            return x
        pow = self.split_pow(x, n // 2)
        if n % 2 == 0:
            return pow * pow
        else:
            return x * pow * pow

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        pow = abs(n)
        flip = n < 0
        ans = self.split_pow(x, pow)
        if flip:
            return 1 / ans
        return ans

        