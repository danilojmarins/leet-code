class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        
        # keep track of last element in both lists
        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            
            index = j + i + 1

            if nums2[i] >= nums1[j]:
                nums1[index] = nums2[i]     # greater element is in nums2 and moved end of nums1
                i -= 1                      # point to previous element of nums2
            else:
                nums1[index] = nums1[j]     # greater element is in nums1 and moved end of nums1
                j -= 1                      # point to previous element of nums1

        if j == -1:
            nums1[0] = nums2[i]             # nums1 is empty or pointer out of bounds