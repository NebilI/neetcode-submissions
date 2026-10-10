from functools import cache


class Solution:

    def checkValidString(self, s: str) -> bool:

        

        @cache
        def check(stack_size, i):
            if stack_size < 0:
                return False
           
            for t, c in enumerate(s[i:], start = i):
                if c == "(":
                    stack_size += 1
                elif c == ")":
                    if stack_size == 0:
                        return False
                    else:
                        stack_size -= 1
                else:
                    return any(check(stack_size + x, t + 1) for x in (-1,0,1) )
            
                if stack_size < 0:
                    return False

            
            return stack_size == 0
        
        return check(0, 0)