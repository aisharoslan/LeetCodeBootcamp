#Medium
#Approach 1: Brute Force (TIME LIMIT EXCEEDED)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            chars = set()
            for i in range(start, end + 1):
                if s[i] in chars:
                    return False
                chars.add(s[i])
            return True

        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if check(i, j): 
                    #basically a nested for loop, true if not repeated yet
                    res = max(res, j - i + 1) #sliding window size
        return res

#Time: O(n^3)     
#Space: O(min(n,m))

#Approach 2: Sliding Window (Accepted)
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #pwwkew
        chars = Counter()
        left = right = 0
        res = 0
        while right < len(s):
            r = s[right] #r = "p", "w", "w""
            chars[r] += 1 #{p:1, w:2} #this is the Counter() dict, no need to initialize to 0

            while chars[r] > 1: #basically will push left up until the duplicate is removed to get new window
                l = s[left] 
                chars[l] -= 1
                left += 1

            res = max(res, right - left + 1)
            right += 1

        return res

#Time: O(n) - worst case each char visited twice by i and j
#Space: O(min(m, n))

#Approach 3: Sliding Window Optimized
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        # mp stores the current index of a character
        mp = {}
        i = 0
        # try to extend the range [i, j]
        for j in range(len(s)): 
            if s[j] in mp:
                i = max(mp[s[j]], i) 

            ans = max(ans, j - i + 1) 
            mp[s[j]] = j + 1 # so if repeated, will go to the index right after that char was first found

        return ans

#Time: O(n) - j will iterate n times
#Space: O(min(m, n))

#Approach 4: Optimized Sliding Window with fixed space
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128 #making an array of size 128 full of None for 128 ascii values
        left = right = 0
        res = 0
        while right < len(s):
            r = s[right]
            index = chars[ord(r)] 
            #stores index of ascii value of s[right] -> will be None if haven't set -> will be = index if alrdy found the char

            if index is not None and left <= index < right:
                left = index + 1 # move up from index if repeated

            res = max(res, right - left + 1)

            chars[ord(r)] = right # set ascii value of s[right] to the curr_index
            right += 1 #move up the string, expand the window
        
        return res

#Time: O(n)
#Space: O(m) - m is size of charset        
        