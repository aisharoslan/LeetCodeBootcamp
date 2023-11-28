#Hard
# Subarray - use sliding window
# Prefix Sum!
from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        min_length = len(nums) + 1
        queue = deque()

        for i in range(len(prefix_sum)):
            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= k:
                min_length = min(min_length, i - queue.popleft())

            while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
                queue.pop()

            queue.append(i)

        return min_length if min_length <= len(nums) else -1

#Approach 2: Monoqueue (Time: O(n), Space: O(n))
class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        prefix_sum = [0]
        for elem in nums:
            prefix_sum.append(prefix_sum[-1] + elem)

        #Want smallest y-x with Py - Px >= K
        ans = len(nums) + 1 # N+1 is impossible
        monoq = deque() #opt(y) candidates, represented as indices of P
        for y, Py in enumerate(prefix_sum): # y is index, Py is the value
            #Want opt(y) = largest x with Px <= Py - K
            while monoq and Py <= prefix_sum[monoq[-1]]:
                monoq.pop()

            while monoq and Py - prefix_sum[monoq[0]] >= k:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < len(nums) + 1 else -1