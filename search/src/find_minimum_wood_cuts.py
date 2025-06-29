# find minimum height so that wood target length of wood will be
# 
# Time complexity: 
# 
# Memory Complexity:

def cut_wood(nums: int, target: int) -> int:
    left, right = 0, len(nums)

    while left < right:

        mid = (left + right) // 2 + 1

        if cut_wood_height(mid, nums, target):
            left = mid
        else:
            right = mid - 1

    return right

def cut_wood_height(minHeight: int, heights: list[int], target: int) -> bool:

    woodlength = 0

    for height in heights:
        if height > minHeight:
            woodlength += (height - minHeight)

    return woodlength >= target



