# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
 

# Constraints:

# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.

class Solution:
    def __init__(self):
        self.memo = {}
    
    def minDistance(self, word1: str, word2: str) -> int:
        if (word1, word2) in self.memo:
            return self.memo[(word1, word2)]

        m = len(word1)
        n = len(word2)

        if m == 0:
            return n
        if n == 0:
            return m

        if word1[m - 1] == word2[n - 1]:
            self.memo[(word1, word2)] = self.minDistance(word1[:m - 1], word2[:n - 1])
        else:
            self.memo[(word1, word2)] = 1 + min(
                self.minDistance(word1[:m - 1], word2),
                self.minDistance(word1, word2[:n - 1]),
                self.minDistance(word1[:m - 1], word2[:n - 1])
            )

        return self.memo[(word1, word2)]