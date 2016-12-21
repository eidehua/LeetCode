'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.
'''
class Solution(object)
    def twoSum(self, nums, target)
        
        type nums List[int]
        type target int
        rtype List[int]
        
        remaining = {}
        for i in range(0, len(nums))
            if nums[i] in remaining
                j = remaining[nums[i]]
                return [j, i]
            remaining[target-nums[i]] = i # dict of [second_num, index]
        return None