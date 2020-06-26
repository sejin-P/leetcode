class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            idx = hmap.get(nums[i])
            if idx:
                return [idx-1,i]
            hmap[target-nums[i]] = i+1