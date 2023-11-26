#Hard
from collections import Counter
#Approach 1: Sliding Window
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #based on constraints, neither s or t will be empty string
        dict_t = Counter(t) #stores the count of each char in t
        required = len(dict_t) #no. of unique char in t, which need to present in desired window
        left = 0
        right = 0
        formed = 0 #keeps track of how many unique char in t are present in curr window in desired freq, eg. if t = "AABC", then window must hv 2 As, 1 B, 1C -> so formed = 3 for 3 unique char when all conditions are met
        window_counts = {} #keeps count of all unique char in curr window
        ans = float("inf"), None, None #ans is a tuple of form (window length, left, right)
        while right < len(s):
            # add 1 char from right to window
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1 #if char in window_counts, then += 1, else, initialize to 0 + 1 = 1

            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1 #so that unique char is satisfied
            
            #only start contracting when all unique char has been met
            while left <= right and formed == required: #once all satisfied, then contract until it stops being "desirable"
                char = s[left]

                #save smallest window till now:
                if (right - left + 1) < ans[0]:
                    ans = (right - left + 1, left, right)
                
                #char at the "left" index is no longer part of window
                window_counts[char] -= 1
                
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1 #so that unique char is no longer satsfied if there is not enough of that char in the curr window

                left += 1 #helps to look for a new window

            right += 1
        
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
        #ans is a tuple - so can index!
        #return substring from left to right + 1 (end non-inclusive)

#Time: O(|S| + |T|) where |S| and |T| represent length of s and t), might end up visiting each char in S twice, once by left, once by right
#Space: O(|S| + |T|) . |S| when window size == len(s).|T| when T has all unique char

#Approach 2: Sliding Window Optimized (evident when |filtered_S| <<<< |S|)
#happens when len(t) way too small than len(s) and s contains a lot of char not in t
#filtered_S only stores the index for char that's in t
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        required = len(dict_t)

        #filter all the char from s that's present in t into a new list along with index as a tuple
        filtered_s = []
        for index, char in enumerate(s): #enumerate gives you a tuple of the index and the thing at that index
            if char in dict_t:
                filtered_s.append((index, char))
        
        left = 0
        right = 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None

        #Look for char only in filtered_s instead of entire s - reduces search
        #Follow sliding window approach on a small list
        while right < len(filtered_s):
            char = filtered_s[right][1]
            window_counts[char] = window_counts.get(char, 0) + 1

            if window_counts[char] == dict_t[char]: #alrdy confirmed gonne be in t - so no need to check here
                formed += 1
            
            #if curr window has all char in desired freq
            while left <= right and formed == required:
                char = filtered_s[left][1]

                #save the smallest window until now
                end = filtered_s[right][0] 
                start = filtered_s[left][0]
                if (end - start + 1) < ans[0]:  
                    ans = (end - start + 1, start, end) 

                window_counts[char] -= 1
                if window_counts[char] < dict_t[char]:
                    formed -= 1
                
                left += 1

            right +=1
        
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

#Time: O(2 * |filtered_S| + |S| + |T|)
#Space: O(|S| + |T|)