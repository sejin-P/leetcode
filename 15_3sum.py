class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        for i in range(n):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                sum_result = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                if sum_result < 0:
                    l += 1
                elif sum_result > 0:
                    r -= 1
                else:
                    answer.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    while l < n-1 and sorted_nums[l] == sorted_nums[l+1]:
                        l += 1
                    while r > 1 and sorted_nums[r] == sorted_nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return answer