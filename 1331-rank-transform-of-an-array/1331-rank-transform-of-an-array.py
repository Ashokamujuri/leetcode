class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_sorted = sorted(list(set(arr)))        
        rank_map = {num: i + 1 for i, num in enumerate(unique_sorted)}        
        return [rank_map[num] for num in arr]