class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = [nums[0]]
        right = [nums[-1]]
        l = len(nums)

        for x in range(1,l):
            left.append(left[-1]+ nums[x])
            right.append(right[-1] + nums[l-1-x])

        right = right[::-1]

        for i in range(l):
            if l == 1:
                return 0
            elif i == 0:
                lef = 0
                rig = right[i+1]
            elif i == l-1:
                lef = left[i-1]
                rig = 0
            else:
                lef = left[i-1]
                rig = right[i+1]

            if lef == rig:
                return i

        return -1
      
