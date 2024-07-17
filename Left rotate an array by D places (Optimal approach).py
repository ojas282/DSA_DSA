class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        def reverseed(nums,start,end):
            while start<=end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1

        k=k%n
        reverseed(nums, 0, n - k - 1)
        reverseed(nums, n - k, n - 1)
        reverseed(nums, 0, n - 1)
        return nums
        