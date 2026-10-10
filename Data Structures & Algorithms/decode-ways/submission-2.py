from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def sub_num_decodings(i):
            if len(s[i:]) == 0:
                return 0
            if s[i] == '0':
                return 0
            if len(s[i:]) == 1:
                    return 1
            if len(s[i:]) == 2:
                    num = s[i:]
                    if num[0] == '1':
                        if num[1] == '0':
                            return 1
                        else:
                            return 2

                    if num[0] == '2':
                        if num[1] in ('0', '7', '8', '9'):
                            return 1
                        else:
                            return 2 

            if s[i] not in ('1', '2'):
                return sub_num_decodings(i + 1)
            else:
                if s[i] == '1':
                    return sub_num_decodings(i + 1) + sub_num_decodings(i + 2)
                else:
                    if s[i+1] in ('0', '7', '8', '9'):
                        return sub_num_decodings(i + 2)
                    else:
                        return sub_num_decodings(i + 1) + sub_num_decodings(i + 2)
        
        return sub_num_decodings(0)
                        