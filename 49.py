class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        anagrams = {}
        
        for ele in strs:

            sorted_element = tuple(sorted(ele))
            if sorted_element in anagrams:
                anagrams[sorted_element].append(ele)
            else:
                anagrams[sorted_element] = [ele]

        return list(anagrams.values())

    
strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
print(sol.groupAnagrams(strs))
        