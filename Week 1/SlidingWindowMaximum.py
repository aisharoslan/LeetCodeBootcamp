# Hard
# Approach 1: Brute Force (TIME LIMIT EXCEEDED)
# n - k + 1 windows and O(k) to find largest element from each window
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        left = 0
        right = 0 + k - 1
        ans = []
        while right < len(nums):
            maxNum = -10000 # min. determined by the question
            for i in range(left, right + 1):
                maxNum = max(nums[i],maxNum)
            ans.append(maxNum)
            left += 1
            right += 1

        return ans

#Time: O(kn) - Worst Case, else, O(k * (n-k+1))
#Space: O(n)

from collections import deque
# Approach 2: Monotonic Deque
# Always sorted - we want a decreasing queue
# Remove all elements less than x before adding x
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque() #largest element at index 0 #only stores useful elem
        res = [] #to store answer
        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]: #gets last elem 
                dq.pop() 
            
            dq.append(i)
        
        res.append(nums[dq[0]])
        
        for i in range(k, len(nums)):
            if dq and dq[0] == i - k: 
                dq.popleft() # pop the first elem
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            
            dq.append(i)
            res.append(nums[dq[0]])
            
        return res

#Time: O(n) - eventho nested while loop - each elem only added to deque once - max is n pushes - every iteration of while loop uses 1 pop - never more than n times in total - every element pushed and popped once - O(2n) = O(n)
#Space: O(k) - size of deque is max size k