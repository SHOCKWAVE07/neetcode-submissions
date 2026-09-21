class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums)-1
        top = -1
        while s<e:
            mid = s + (e-s)//2
            print(nums[mid])
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                top = mid
                break

            elif nums[s]>nums[mid]:
                e = mid
            
            else:
                s = mid+1

        return nums[top+1]
