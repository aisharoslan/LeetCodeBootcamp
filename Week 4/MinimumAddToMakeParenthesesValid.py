#Medium
#Approach 1: Stack
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            else:
                if stack and stack[-1] == '(': #not empty and peek is (
                    stack.pop() #pop once get a set of ()
                else:
                    stack.append(char)
        return len(stack) #remaining parentheses with no pair

#Time: O(n)
#Space: O(n) #for stack

#Approach 2: Balance
#Keep track of balance = # of '(' - # of ')', valid if balance = 0
class Solution(object):
    def minAddToMakeValid(self, s):
        ans = balance = 0
        for symbol in s:
            balance += 1 if symbol == '(' else -1
            if balance == -1:
                ans += 1
                balance += 1
        return ans + balance

#Time: O(n)
#Space: O(1)