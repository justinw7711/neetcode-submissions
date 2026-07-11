class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        length = m+n
        arr = length*[0]
        newA = nums1[:m]
        mergeA = newA + nums2
        mergeA.sort()
        nums1[:] = mergeA
        """
        Do not return anything, modify nums1 in-place instead.
        """
        