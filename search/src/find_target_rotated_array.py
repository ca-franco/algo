## Find the target from a rotatable array.
##
## Time complexity:O(log(n))
## Memory complexity: 0(1)
##


def find_target_from_rotatable_array(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return left if nums and nums[left] == target else -1

