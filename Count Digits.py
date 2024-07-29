# Given a number n. Count the number of digits in n which evenly divide n. Return an integer, total number of digits of n which divides n evenly.

# Note :- Evenly divides means whether n is divisible by a digit i.e. leaves a remainder 0 when divided.
 

# Examples :

# Input: n = 12
# Output: 2
# Explanation: 1, 2 when both divide 12 leaves remainder 0.
# Input: n = 2446
# Output: 1
# Explanation: Here among 2, 4, 6 only 2 divides 2446 evenly while 4 and 6 do not.
# Input: n = 23
# Output: 0
# Explanation: 2 and 3, none of them divide 23 evenly.
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)
 

# Constraints:
# 1<= n <=105

#User function Template for python3

#Approach 1
class Solution:
    def evenlyDivides (self, N):
        n = str(N)
        count = 0
        for i in n:
            if int(i)==0:
                continue
            elif N%int(i)==0:
                count+=1

        return count

class Solution:
  
                
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends