#Medium

# #Approach 1: Brute Force Solution - NOT ACCEPTED (Time Limit Exceeded)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea = 0 # max height x max width #O(1)
        for i in range(len(height)): #O(n)
            for j in range(i + 1, len(height)): #O(n - 1)
                width = j - i 
                maxArea = max(maxArea, min(height[i], height[j]) * width)
                #need the min height to see which one is shorter
        return maxArea

#Time: O(n^2) -> #O(n(n-1)/2)
#Space: O(1)      

#Approach 2: Two Pointer Approach
class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea = 0 # max height x max width #O(1)
        left = 0
        right = len(height) - 1
        while left <= right: #O(n)
            width = right - left
            maxArea = max(maxArea, min(height[left], height[right]) * width)
            if height[left] <= height[right]: #get higher height to overcome reduced width
                left += 1
            else:
                right -= 1

        return maxArea

#Time: O(n)
#Space: O(1)