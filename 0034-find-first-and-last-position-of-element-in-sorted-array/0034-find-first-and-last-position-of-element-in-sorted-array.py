class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstOccurrence(arr, n, k):
            low, high = 0, n - 1
            first = -1
            
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == k:
                    first = mid
                    high = mid - 1  # Continue searching towards the left
                elif arr[mid] < k:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            return first

        def lastOccurrence(arr, n, k):
            low, high = 0, n - 1
            last = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == k:
                    last = mid
                    low = mid + 1  # Continue searching towards the right
                elif arr[mid] < k:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            return last

        n = len(nums)
        first = firstOccurrence(nums, n, target)
        last = lastOccurrence(nums, n, target)
        
        return [first, last]