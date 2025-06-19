# Search and Sorting

## Binary Search
Binary search for target in an array which is already sorted.

<pre>'''python
def findTarget(nums: List[int], target: int) -> int:

    left, right = 0, len(nums)

    while left < right:
        median = (left + right) // 2
        
        if target > nums[median]:
            left = median
        elif target < nums[median]:
            right = median
        else:
            return nums[median]
    return -1
'''
</pre>
