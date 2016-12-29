'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Saying 342 + 465 = 807

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        '''
        342 + 465 = 807
        what about different length inputs?
        1342 + 465 = 
        (2->4->3->1) + (5->6->4)
        7->0->8->1
        '''
        carry = 0
        l3_head = None
        l3_prev = None 
        while True:
            #print l3_prev
            #print l3_head
            if l1 == None and l2 == None:
                # done with both lists
                # deal with final carry
                if carry == 1:
                    l3_prev.next = ListNode(1)
                return l3_head
            if l1 == None:
                value1 = 0
            else:
                # update value, move to next node
                value1 = l1.val
                l1 = l1.next
            if l2 == None:
                value2 = 0
            else:
                value2 = l2.val
                l2 = l2.next
                
            sum = value1 + value2 + carry
            new_digit = sum % 10
            carry = sum/10 # either 1 or 0
            if l3_prev == None:
                l3_prev = ListNode(new_digit) # update what l3_prev refers to
                l3_head = l3_prev
            else: 
                l3_prev.next = ListNode(new_digit)
                l3_prev = l3_prev.next
            
        
        