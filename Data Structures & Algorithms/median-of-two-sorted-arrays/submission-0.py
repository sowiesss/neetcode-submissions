class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        mid = (m + n) // 2
        odd = (m + n) % 2
        i, j = 0, 0
        s = 0 if odd else 1

        while i < m and j < n and i + j < mid - s:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        m1, m2 = 0, 0
        if((i < m and j < n and nums1[i] < nums2[j])
            or j >= n):
            m1 = nums1[i]
            i += 1
        else:
            m1 = nums2[j]
            j += 1
        
        res = m1
        if not odd:
            if ((i < m and j < n and nums1[i] < nums2[j])
                or j >= n):
                m2 = nums1[i]
                res = (m1 + m2) / 2
            else:
                m2 = nums2[j]
                res = (m1 + m2) / 2
       
        return res

