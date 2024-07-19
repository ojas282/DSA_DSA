# 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Approach 1

        # n=len(nums)
        # arr=[]
        # #making another array to store range
        # for i in range(n+1):
        #     arr.append(i)
        # set1=set(nums)
        # set2=set(arr)
        # diff = list(set2-set1)
        # if len(diff)==1:
        #     return(diff[0])

        #Approach 2

        n=len(nums)
        sumOfRange=(n*(n+1))/2
        sumOfNums=sum(nums)
        return(int(sumOfRange-sumOfNums))
        
        