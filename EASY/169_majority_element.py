class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        elements = {}                               # dict store elements and occurences

        for num in nums:                            # increase the occurence of each element
            if num in elements:
                elements[num] = elements[num] + 1
            else:
                elements[num] = 1

        keys = list(elements.keys())                # list of elements
        values = list(elements.values())            # list of its occurences

        return keys[values.index(max(values))]      # element with most occurences

## Time Complexity = O(n)