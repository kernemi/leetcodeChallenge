class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}
        for x,y in enumerate(nums):
            rev = target - y

            if rev in dicts:
                return [x,dicts[rev]]
            
            dicts[y] = x

