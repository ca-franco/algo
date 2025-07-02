# Search

## Binary Search
Binary search for target in an array which is already sorted.

> Note:
> The search space is mostly the explict but at times it can be implict


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

Time Complexity: O(log(n)
Space Complexity: O(1)

## Different problem sets which need implict and explicit search spaces
-   Sorted Arrays
    -   [First and last occurence of the a Number](src/find_first_last_occurrence_of_number.py)
    -   [Find the insertion index](src/find_insertion_index.py)
-   Partially sorted Arrays
    -   [Find the target in rotated sorted array](src/find_target_rotatable_array.py)
-   Non-intiutive search
    -   [Cutting Wood](src/find_minimum_wood_cuts.py)
    -   Local maxima in Array
-   Multiple arrays
    -   [Find the median from two sorted arrays](src/find_median_from_two_sorted_array.py)
-   Matrix search
    -   [Matrix search](src/matrix_search.py)
-   More problems for implicit search space
    -   [Sqrt(x) find the square root of x](src/find_sqrt.py)
    -   Valid prefect squares
    -   Arranging coins
