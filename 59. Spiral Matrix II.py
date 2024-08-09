# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

# Example 1:


# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:

# Input: n = 1
# Output: [[1]]
 

# Constraints:

# 1 <= n <= 20

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

    
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        rowBegin = 0
        rowEnd = n-1
        colBegin = 0
        colEnd = n-1
        square = n*n
        arr=[]
        final_matrix = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(1,square+1):
            arr.append(i)
        ptr = 0

        while(rowBegin<=rowEnd and colBegin<=colEnd):

            #Traversing the matrix from left to right
            for i in range(colBegin,colEnd+1):
                final_matrix[rowBegin][i]=arr[ptr]
                ptr+=1
            rowBegin+=1

            #Traversing the matrix from top to bottom
            for i in range(rowBegin,rowEnd+1):
                final_matrix[i][colEnd]=arr[ptr]
                ptr+=1
            colEnd-=1

            if colBegin<=colEnd:

                #Traversing the matrix from right to left
                for i in range(colEnd,colBegin-1,-1):
                    final_matrix[rowEnd][i] = arr[ptr]
                    ptr+=1
            rowEnd-=1

            if rowBegin<=rowEnd:
                #Traversing the matrix from bottom to top
                for i in range(rowEnd,rowBegin-1,-1):
                    final_matrix[i][colBegin] = arr[ptr]
                    ptr+=1
            
            colBegin+=1
                
        return final_matrix
