class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        records = {}

        for n in nums:
            if n in records:
                records[n] += 1
            else:
                records[n] = 1
        
        for count in records.values():
            if count > 1:
                return True
        
        return False