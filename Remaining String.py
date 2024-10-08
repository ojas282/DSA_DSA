# Remaining String
# Difficulty: EasyAccuracy: 17.06%Submissions: 56K+Points: 2
# Given a string s without spaces, a character ch and an integer count. Your task is to return the substring that remains after the character ch has appeared count number of times.
# Note:  Assume upper case and lower case alphabets are different. “”(Empty string) should be returned if it is not possible, or the remaining substring is empty.

# Examples:

# Input: s = "Thisisdemostring", ch = 'i', count = 3
# Output: ng
# Explanation: The remaining substring of s after the 3rd
# occurrence of 'i' is "ng", hence the output is ng.
# Input: s = "Thisisdemostri", ch = 'i', count = 3
# Output: ""
# Explanation: The 3rd occurence of 'i' is at the last index. In this case the remaining substring is empty, hence we return empty string.
# Input: s = "abcd", ch = 'x', count = 2
# Output: ""
# Explanation: The character x is not present in the string, hence we return empty string.
# Expected Time Complexity: O(|s|)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1<= s.length()<=105
# 1<=count<=s.length()
# s[i] is both upper case and lower case

#User function Template for python3
class Solution:
	def printString(self, s, ch, count):
	    occ = 0
	    st=''
	    for i in range(0,len(s)):
	        if s[i]==ch:
	            occ=occ+1
	        if occ==count:
	            break
	    if i<len(s)-1:
	        st = s[i+1:]
	        return st
	    else:
	        return ""
		                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ch = input()[0]
        count = int(input())
        ob = Solution()
        answer = ob.printString(s, ch, count)

        print(answer)

# } Driver Code Ends