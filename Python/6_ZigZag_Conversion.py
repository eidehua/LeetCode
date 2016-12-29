'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        """
        P   A   H   N   0, 4, 8, 12  (0 + numRows + numZigs)
        A P L S I I G   1, 3, 5, 7, 9, 11, 13  -> 1, 5, 9, 13 | 3 (numRows), 7, 11
        Y   I   R       2, 6, 10
        """
        """
        P     H         0, 8 (0 + numRows + numZigs) = 8 numZigs = numRows - 2
        A   S I         1, 7, 9 -> 1, 9 | 7 (numRows + 2)
        Y  I  R         2, 6, 10 -> 2, 10 | 6 (numRows + 1)
        P L   I G       3, 5, 11, 13 -> 3, 11 | 5 (numRows), 13  
        A     N         4, 12
        
        """
		'''
			Algorithm idea:
			We want to add the elements in the first row first
			Then find add elements of the second row
			Then find add elements of the third row
			and so on
			
			So to get the PAHN of first row out of PAYPALISHIRING
			WE grab the upper case letter: PaypAlisHiriNg. There are (3) chars between row elements!
			(3) = numRows
		'''
        result_list = []
        
        #0,... rows-1
        for start_index in xrange(0, numRows):
            index = start_index
            while(index < len(s)):
                result_list.append(s[index])
                index += numRows
        
        # print ''.join(result_list)
        return ''.join(result_list)