# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

 

# Example 1:

# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:

# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# Example 3:

# Input: s = "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '(' or ')'.
# s is a valid parentheses string.

class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        
        ans = ""
        count = 0
        for i in s:  
            if i =="(":
                count+=1 #increment count as soon as we find "("
                if count > 1:  #check if count is greater than one that would mean that "(" is not the outer parantheses hence include it in our answer
                    ans=ans+i #including i in our answer
            elif i ==")":  
                count-=1 #decrement count as soon as we find ")" 
                if count>0: #check is the count is greater than 0, is so then append ")" in our answer as well
                    ans=ans+i
        return ans