class Solution:
    def twoSum(self, nums:list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            if nums[i] + nums[i+1] == target:
                    return [i,i+1]
s=Solution()
print(s.twoSum([2,7,11,15],9))
         