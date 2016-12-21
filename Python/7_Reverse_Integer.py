class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # Work with the abs(value) for easier transfer of digits
        # 123
        # 123/10 -> 12/10 -> 1. 1 < 10. Extract
        # 123 % 100 = 23
        # 23/10 -> 2. 2 < 10. Extract
        # 23 % 10 -> 3. 3 < 10. Extract
        #
        # 1 + 2*10 + 3*100 = 321
        
        # Better way, that also should work with numbers like 101
        # 123 % 10 -> 3 (extract)
        # 123/10 -> 12
        # 12 % 10 -> 2 (extract)
        # 12 / 10 -> 1
        # 1 % 10 -> 1 (extract)
        # 1 / 10 -> 0 (done)
        
        '''
            ** important ** extracted 3, then 2, then 1
            But want to build 123!!!
            So keep track of reversed like so.
            Reversed = 0
            Reversed = 1
            Reversed = 12 (10*1 + 2)
            Reversed = 123 (10*12 + 3)
        
        '''
        
        # What about when the reverse overflows? So for 32 bit integer, reverse of 1000000003 overflows
        # when adding to get the reversed integer, if sign changes, then we are in bad shape!
        
        
        # What about 10?
        # 10/10 -> 1. 1 < 10. Extract
        # 10% 10 = 0. Extract a 0.
        # 1 + 10*0 = 0
        
        # What about 100? -> 001
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)    
        reversed = 0
        
        multiplier = 1
        while x > 0:
            # extract least significant digit
            digit = x % 10
            x /= 10
            reversed *= 10
            reversed += digit               # eg 0 -> 0+1=1 -> 10+2=12 -> 120+3 = 123, reverse of 321
            
            # quick hack since python default overflows int to long
            if reversed > 2147483648:
                return 0
        if reversed > 2147483648:
            return 0
        return reversed * sign