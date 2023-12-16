class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        entries = {}                # dict / hash map with each element of nums

        for num in nums:            # number of occurences of each element in nums
            if num in entries:
                entries[num] += 1
            else:
                entries[num] = 1
        
        index = 0

        for entry in entries:           
            if entries[entry] == 1:     # if element appears once, assign once to nums
                nums[index] = entry
                index += 1
            elif entries[entry] > 1:    # if element appears more than once, assign twice to nums
                nums[index] = entry
                index += 1
                nums[index] = entry
                index += 1
        
        return index

## Time Complexity = O(2n) -> O(n)