from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m > 0 or n > 0:
            if m == 0:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            elif n == 0 or nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1