class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        nums1 [2, 5, 7, 0, 0, 0, 0]
        nums2 [-2, -1, 4, 8]
        m = 3
        m = 4

        expected output = [-2, -1, 2, 4, 5, 7, 8]

        """

        free = m + n  - 1   # keep track of last insertable space

        # two pointers
        n -= 1
        m -= 1

        while n >= 0 and m >= 0:

            if nums2[n] >= nums1[m]:
                nums1[free] = nums2[n]
                n -= 1
            else:
                nums1[free] = nums1[m]
                nums1[m] = 0
                m -= 1
            free -= 1
            
        if m == -1:         # nums1 reached end
            while n >= 0:
                nums1[n] = nums2[n]
                n -= 1
            return