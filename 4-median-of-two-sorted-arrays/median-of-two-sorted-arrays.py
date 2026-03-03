class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = list(heapq.merge(nums1, nums2))
        arr_len = len(merged_array)

        median = None

        if arr_len % 2 == 0:
            mid_ind = int(arr_len / 2)
            median = (merged_array[mid_ind] + merged_array[mid_ind - 1]) / 2
        else:
            mid_ind = int(arr_len // 2)
            median = merged_array[mid_ind]
        return median