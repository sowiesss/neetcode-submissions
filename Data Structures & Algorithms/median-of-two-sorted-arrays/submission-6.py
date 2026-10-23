class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        A, B = nums1, nums2
        if m > n:
            A, B = B, A
            m, n = n, m

        mid = (m + n + 1) // 2 
        odd = (m + n) % 2
        
        l, r = 0, m
        while l <= r:
            p1 = (l + r) // 2
            p2 = mid - p1
           
            Aleft = A[p1 - 1] if p1 > 0 else float("-infinity")
            Aright = A[p1] if p1 < m else float("infinity")
            Bleft = B[p2 - 1] if p2 > 0 else float("-infinity")
            Bright = B[p2] if p2 < n else float("infinity")
            print(p1, p2, Aright, Bright, Aleft, Bleft)
            if Aleft <= Bright and Bleft <= Aright:
                if odd:
                    return max(Aleft, Bleft)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = p1 - 1
            else:
                l = p1 + 1
        return 0.0