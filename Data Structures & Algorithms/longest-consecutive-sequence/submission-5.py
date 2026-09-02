class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) 
        length = 0
        for num in nums:
            # is this first element
            if num - 1 not in nums_set: 
                streak = 1
                current = num
                # Streak Logic
                while (current + 1 in nums_set):
                    streak += 1
                    current += 1

                length = max(length, streak)
        return length
                