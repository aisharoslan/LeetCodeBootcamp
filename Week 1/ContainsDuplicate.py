#Easy

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_set = set()
        for num in nums: #O(n)
            if num in hash_set: #O(1) to find for set
                return True
            else:
                hash_set.add(num) #O(1)
        return False

#Time: O(n)
#Space: O(n)