class Solution:
    def bsearch(self, nums, target):
        s = 0
        e = len(nums)-1

        while s<=e:

            mid = s + (e-s)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                e = mid - 1
            else:
                s = mid+1
        
        return -1

    def search(self, nums: List[int], target: int) -> int:

        s = 0
        e = len(nums)-1
        top = -1

        while s<e:

            mid = s + (e-s)//2

            if nums[mid-1]<nums[mid]>nums[mid+1]:
                top = mid
                break
            
            elif nums[mid]>nums[s]:
                s = mid+1
            else:
                e = mid


        l = self.bsearch(nums[:top+1],target)
        r = self.bsearch(nums[top+1:],target)

        if l == -1 and r == -1:
            return -1
        elif l== -1:
            return top+1 + r
        else:
            return l


        