#Easy
class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        for i in edges[0]:
            if i in edges[1]:
                return i
# #Time: O(n)
# #Space: O(1)

class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        if edges[0][0] in edges[1]: 
            return edges[0][0]
        return edges[0][1]  
#Time: O(1)
#Space: O(1)      

class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        firstEdge = edges[0]  
        secondEdge = edges[1]   

        elem1, elem2 = firstEdge #each edge[i] has length 2 only
        if elem1 in secondEdge:
            return elem1  
        return elem2
#Time: O(2) = O(1) #max times is 2 to check for existence
#Space: O(1)