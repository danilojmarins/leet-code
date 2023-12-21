class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        i = 0               # keep track of current
        curr = nums[i]      # current is 1st element

        for count in range(len(nums)):              # repeat until every element is rotated
            _next = (i + k) % len(nums)             # position to rotate current to
            
            temp = nums[_next]                      # stores the next element
            nums[_next] = curr                      # replace next element with current
            curr = temp                             # assign replaced to current
            i = _next                               # current position is updated

            if ((count + 1) * k) % len(nums) == 0:  # current returned to already rotated element, pick next
                i = (i + 1) % len(nums)
                curr = nums[i]

## Time Complexity = O(n)