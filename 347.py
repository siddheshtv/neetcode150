class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums = sorted(nums)
        freq = {}
        for ele in nums:
            if ele in freq:
                count = count + 1
                freq[ele] = count
            else:
                count = 1
                freq[ele] = count
        
        ls = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        print(freq)
        print(ls)
        return ls[:k]


sol = Solution()
print(sol.topKFrequent(nums = [4,1,-1,2,-1,2,3], k = 2))