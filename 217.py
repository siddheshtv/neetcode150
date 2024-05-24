# 217 Duplicate Integer
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num = set()
        for ele in nums:
            if ele in num:
                return True
            num.add(ele)
        return False
    
    def containsDuplicate2(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))

sol = Solution()
print(sol.containsDuplicate(nums=[1,2,3,1]))