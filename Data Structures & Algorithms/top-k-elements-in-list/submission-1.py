class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        res = []

        for n, cnt in count.items():
            res.append([cnt, n])
        
        res.sort(reverse=True)
        
        return [n for cnt, n in res[:k]]