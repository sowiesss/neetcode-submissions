class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        mid = (m + n + 1) // 2 # round up
        odd = (m + n) % 2
        i, j = 0, 0
        
        for c in range(1, mid):
            if j >= n or (i < m and nums1[i] < nums2[j]):
                i += 1
            else:
                j += 1
            
        m1, m2 = 0, 0
        if(j >= n or (i < m and nums1[i] < nums2[j])):
            m1 = nums1[i]
            i += 1
        else:
            m1 = nums2[j]
            j += 1
        
        res = m1
        if not odd:
            if (j >= n or (i < m and nums1[i] < nums2[j])):
                m2 = nums1[i]
                res = (m1 + m2) / 2
            else:
                m2 = nums2[j]
                res = (m1 + m2) / 2
       
        return res

