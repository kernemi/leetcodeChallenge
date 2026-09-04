class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new = [nums[0]]
        for x in range(1,len(nums)):
            new.append(new[-1]+nums[x])
        return new
