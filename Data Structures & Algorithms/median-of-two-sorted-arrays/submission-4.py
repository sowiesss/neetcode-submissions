class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        m1 = (m + n + 1) // 2
        odd = (m + n) % 2
        if odd:
            return self.findKthSmallest(nums1, m, nums2, n, 0, 0, m1)
        else:
            return (self.findKthSmallest(nums1, m, nums2, n, 0, 0, m1) + self.findKthSmallest(nums1, m, nums2, n, 0, 0, m1 + 1) ) / 2
        
    
    def findKthSmallest(self, alist, asize, blist, bsize, astart, bstart, k):
        if asize > bsize:
            return self.findKthSmallest(blist, bsize, alist, asize, bstart, astart, k)

        if asize == 0:
            return blist[bstart + k - 1]
        
        if k == 1:
            return min(alist[astart], blist[bstart])
        
        i = min(asize, k // 2)
        j = min(bsize, k // 2)

        if alist[astart + i - 1] < blist[bstart + j - 1]:
            return self.findKthSmallest(alist, asize - i, blist, bsize, astart + i, bstart, k - i)
        else:
            return self.findKthSmallest(alist, asize, blist, bsize - j, astart, bstart + j, k - j)