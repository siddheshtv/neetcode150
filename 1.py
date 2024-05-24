# Two Sum
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = {}
        for i,x in enumerate(nums):
            y = target - x
            if y in hash:
                return [hash[y], i]
            else:
                hash[x] = i 
                

sol = Solution()
print(sol.twoSum(nums=[2,5,5,11], target=10))