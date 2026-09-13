class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_index_zero=0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[non_index_zero] = nums[non_index_zero],nums[i]
                non_index_zero+=1
        return nums
