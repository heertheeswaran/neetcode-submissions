class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Index = frequency, value = list of numbers with that frequency
        # Max frequency can't exceed len(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        # Iterate from highest frequency to lowest
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res