class Solution:
    def sum_squares_of_digits(self, t):
        return sum(int(x) **2 for x in str(t))

    def isHappy(self, n: int) -> bool:

        previous = set()

        while True:

            n = self.sum_squares_of_digits(n)

            if n == 1:
                return True
            if n in previous:
                return False
            previous.add(n)
        
        return False
        