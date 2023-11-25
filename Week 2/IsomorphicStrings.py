#Easy
# Rules:
# 1. Can map a char only to itself or one other char (no changing after mapped)
# 2. No two char should map to same char
# 3. Replace each char in string s with char it is mapped to results in string t
# 4. Need 1-1 mapping - need to consider vice versa too - so have a map for s to t and map for t to s
# 5. If not same length -> not isomorphic - return false - but in this case, same length 

# Approach 1: Character Mapping with Dictionary
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}
        for i in range(len(s)):
            #Case 1: No mapping exists in either dict
            if (s[i] not in s2t) and (t[i] not in t2s):
                s2t[s[i]] = t[i]
                t2s[t[i]] = s[i]
            
            #Case 2: Either mapping doesn't exist or mapping exists and doesn't match in either of the dict or both
            elif s2t.get(s[i]) != t[i] or t2s.get(t[i]) != s[i]:
                return False
        
        return True

#Time: O(n) - process each char in both strings exactly once
#Space: O(1) - ascii char set is fixed, eg O(26) = O(1)

# Approach 2: First occurrence transformation - modify to the index,
# eg. paper = title = 01034
class Solution:
    def transformString(self, s: str) -> str:
        index_map = {}
        new_str = []

        for i in range(len(s)):
            if s[i] not in index_map:
                index_map[s[i]] = i
            
            #no "else:" bc we want it to still append if s[i] not in index_map
            new_str.append(str(index_map[s[i]]))

        return " ".join(new_str)

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)

#Time: O(n) - process each char in both strings exactly once
#Space: O(n) - form 2 new strings = O(2n) = O(n) - size of ASCII char set is fixed - size of map in the transform func x contribute to space complexity