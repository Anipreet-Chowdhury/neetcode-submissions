class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = [set() for i in range(len(nums)+1)]
        for val in nums:
            ct = nums.count(val)
            occurences[ct].add(val)
        occurences = [list(x) for x in occurences if x != set()]
        res = []
        for i in occurences:
            for val in i:
                res.append(val)
        return res[-k:]

        
        
        


