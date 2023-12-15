class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 1                               # 1st element is already correct
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:            # next is non-duplicate
                nums[index] = nums[i+1]
                index += 1
        return index
    
## Time Complexity = O(n)
## Runtime = 80ms -> Beats 82%
## Memory = 17.9MB -> Beats 42%