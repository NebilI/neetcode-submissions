class Solution:
    def str_to_int(self, num: str) -> int:
        num_int = 0
        mult = 1
        base = ord('0')
        for c in num[::-1]:
            i = ord(c) - base 
            num_int += mult * i
            mult *= 10
        return num_int

    def multiply(self, num1: str, num2: str) -> str:
        return str(self.str_to_int(num1) * self.str_to_int(num2))
        