class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
        s = 0
        e = len(nums)

        while s<e:
            mid = s + (e-s)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                e = mid
            else:
                s = mid + 1

        return -1
        