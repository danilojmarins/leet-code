class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = len(nums)
        free = len(nums) - 1   # free spaces - end of list
        i = 0

        while i <= free:
            if nums[i] != val:  # continue loop - verify next
                i += 1
                continue

            if nums[i] == val and free == i:    # doesnt swap
                free -= 1
                k -= 1
                i += 1
                continue

            if nums[i] == val:
                if nums[free] == val:   # free space equals val - doesnt update i
                    nums[free] = 0
                    free -= 1
                    k -= 1
                    continue
                else:                   # swap free and val
                    nums[i] = nums[free]
                    nums[free] = 0
                    free -= 1
                    k -= 1
                    i += 1
                    continue

        return k
    
## Time Complexity = O(n)
## Runtime = 37ms -> Beats 78%
## Memory = 16.3MB -> Beats 52%