## Time complexity: O(log(n))
## Space complexity: O(1)

def find_the_insertion_index(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        # For any case if target is on mid or less
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1

    return left

