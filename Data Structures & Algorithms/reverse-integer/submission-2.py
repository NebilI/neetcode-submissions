class Solution:
    def in_range(self, x):
        min_range = str(-(2 ** 31))
        max_range = str(2 ** 31 - 1)
        str_x = str(x)
        if x[0] == "-":
            if len(str_x) < len(min_range):
                return True
            if len(str_x) > len(min_range):
                return False

            for i in range(1,len(min_range)):
                if ord(min_range[i]) > ord(str_x[i]):
                    return True
                if ord(min_range[i]) < ord(str_x[i]):
                    return False
            
            return True
        
        else:
            if len(str_x) < len(max_range):
                return True
            if len(str_x) > len(max_range):
                return False

            for i in range(0,len(max_range)):
                if ord(max_range[i]) > ord(str_x[i]):
                    return True
                if ord(max_range[i]) < ord(str_x[i]):
                    return False
            
            return True            
        
        return True
                

    def reverse(self, x: int) -> int:
        t = abs(x)
        sign = -1 if x < 0 else 1
        
        if not self.in_range(("-" if sign -1 else "") + str(t)[::-1]):
            return 0
        else:
            if x < 0:
                return -int(str(t)[::-1])
            else:
                return int(str(t)[::-1])