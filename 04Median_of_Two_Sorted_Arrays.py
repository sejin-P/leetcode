def findMedian(small_array, big_array):
    m = len(small_array)
    n = len(big_array)
    half = (m+n+1) // 2
    min_i, max_i = 0, m
    while (min_i <= max_i):
        i = (min_i + max_i) // 2
        j = half - i
        
        if (i < max_i and big_array[j-1] > small_array[i]):
            min_i += 1
        elif (i > min_i and big_array[j] < small_array[i-1]):
            max_i -= 1
        else:
            if i == 0:
                left_max = big_array[j-1]
            elif j == 0:
                left_max = small_array[i-1]
            else:
                left_max = max(small_array[i-1], big_array[j-1])
            if (m+n) % 2 == 1:
                return left_max
            if i == m:
                right_min = big_array[j]
            elif j == n:
                right_min = small_array[i]
            else:
                right_min = min(big_array[j], small_array[i])
            
            if (m+n) % 2 == 0:
                return (left_max + right_min) / 2
            

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return findMedian(nums2, nums1)
        else:
            return findMedian(nums1, nums2)