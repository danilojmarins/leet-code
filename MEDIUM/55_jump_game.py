class Solution:
    def canJump(self, nums: list[int]) -> bool:
        curr = 0                                            # current index
        length = len(nums)
        
        for i in range(length):
            _max = 0                                        # max reachable index
            max_index = 0                                   # index of element where max reachable can be achieved
            for j in range(curr + 1, curr + 1 + nums[curr]):
                if j < length and nums[j] + j >= _max:      # loop through curr until max jump length of current
                    _max = nums[j] + j
                    max_index = j                           # save the max reachable index
                if j == length - 1:
                    return True
            curr = max_index
            if curr == length - 1:
                return True

        return False
    
## Time Complexity = O(n²)