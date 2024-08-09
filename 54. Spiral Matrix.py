# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


#include <vector>

using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> v;
        if (matrix.empty() || matrix[0].empty()) return v; // Handle edge case

        int rows = matrix.size();
        int cols = matrix[0].size();

        int colBegin = 0;
        int colEnd = cols - 1;
        int rowBegin = 0;
        int rowEnd = rows - 1;

        while (colBegin <= colEnd && rowBegin <= rowEnd) {
            // Traverse from left to right along the top row
            for (int i = colBegin; i <= colEnd; ++i) {
                v.push_back(matrix[rowBegin][i]);
            }
            rowBegin++;

            // Traverse from top to bottom along the right column
            for (int i = rowBegin; i <= rowEnd; ++i) {
                v.push_back(matrix[i][colEnd]);
            }
            colEnd--;

            if (rowBegin <= rowEnd) {
                // Traverse from right to left along the bottom row
                for (int i = colEnd; i >= colBegin; --i) {
                    v.push_back(matrix[rowEnd][i]);
                }
                rowEnd--;
            }

            if (colBegin <= colEnd) {
                // Traverse from bottom to top along the left column
                for (int i = rowEnd; i >= rowBegin; --i) {
                    v.push_back(matrix[i][colBegin]);
                }
                colBegin++;
            }
        }

        return v;
    }
};
