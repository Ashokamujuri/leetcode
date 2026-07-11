class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reversee(arr, low, high):
            while low < high:
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1
        n = len(nums)  
        k = k % n      
        reversee(nums, 0, n - 1)
        reversee(nums, 0, k - 1)
        reversee(nums, k, n - 1)