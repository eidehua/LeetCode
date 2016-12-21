'''
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.
'''
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        '''
        Feels like a base case and build type of question
        
        I go first. I can remove 1->3 stones
        1: I take 1
        2: I take 2
        3: I take 3
        4: If I take 1, enemy takes 3. He wins
        4: If I take 2, enemy takes 2. He wins
        4: if I take 3, enemy takes 1. He wins.
        5: If i take 1, then enemy is in 4 case. Enemy loses!
        6: If I take 1, enemy is in 5 case, which means he could win. 
        6: If I take 2, enemy is in 4 case, so he loses!
        7: If I take 3, enemy has 4, so no matter what, I win!
        8: If i take 1, 2, or 3 stones, that leaves enemy in 5,6,7 case. so he can always find a way to win!
        
        So I win unless there is 4x stones, where x is >=1
        '''
        
        if n % 4 == 0:
            return False
        return True