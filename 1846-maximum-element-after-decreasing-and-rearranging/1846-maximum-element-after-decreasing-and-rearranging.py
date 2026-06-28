class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        max_val=1
        for i in range(1,len(arr)):
            max_val=min(max_val+1,arr[i])
        return max_val