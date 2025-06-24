### Defining Upper Bound  and Lower Bound
#To understand the niggles for binary search with duplicate numbers let us 
#consider this case:
#
#Assume an array with 1,2,3,4,4,4,5,6 if asked to find the first and last 
#occurence of a target number assume 4 in this case, how should we approach 
#this problem
#
#Time Complexity: O(log(n))
#Memory Complexity: O(1)

def findFirstLastOccurenceOfNumber(nums: List[int], target: int) -> List[int]:
    lowerBoundNumber = findLowerBoundNumberhelper(nums, target)
    upperBoundNumber = findUpperBoundNumberHelper(nums, target)

    return [lowerBoundNumber, upperBoundNumber)

def findLowerBoundNumberhelper(nums, target) -> int:
    left, right = 0, len(nums)-1

    while left < right:
        median = (left + right) // 2
        
        if target < nums[median]:
            right = median - 1
        elif target > nums[median]:
            left = median + 1
        else:
            right = median

    return left if nums and nums[left] == target else -1

def findUpperBoundNumberHelper(nums, target) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            median = ((left + right) // 2) +1
            
            if target < nums[median]:
                right = median - 1
            elif target > nums[media]:
                left = median + 1
            else:
                left = median
        return right if nums and nums[right] == median else -1
