class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        _len = len(nums)
        i = 0                                           # index of current element
        while i < _len:
            num = nums[i]
            if i == _len - 1:                           # current is already last element
                return jumps
            if (i+1) == _len - 1 or num+i+1 > _len - 1: # current max reach (i+num) would already pass last element
                jumps += 1
                return jumps
            if (i+1) < _len and (num+i+1) <= _len:
                max_reach = 0
                max_index = i+1
                for j in range(i+1, num+i+1):           # loop every element reachable from current
                    if nums[j] + j > max_reach:
                        max_reach = nums[j] + j
                        max_index = j
                i = max_index                           # set current to the one which can reach longer in list
                jumps += 1
                continue
        return jumps
    
## Time Complexity = O(n²) -> Beats 86.21%