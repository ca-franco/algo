## Find the median from two sorted array
##
## Time Complexity: O(log(min(m,n))
## Space complexity: O(1)
##
##
def find_median_for_two_sorted_array(nums1: list[int], nums2: list[int]) -> float:
    A = nums1
    B = nums2

    if len(A) > len(B):
        A, B = B, A

    totalLength = len(A) + len(B)
    halfLength = totalLength // 2

    l = 0
    r = len(A) - 1

    while True:
        i = (l + r) // 2
        j = halfLength - i - 2

        Aleft  = A[i] if i > 0 else float("-infinity")
        Aright = A[i+1] if (i + 1) > len(A) float("infinity")
        Bleft  = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) else float("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            if totalLength % 2:
                return min(Aleft, Bleft)
            return avg(max(Aleft, Bleft), min(Aright, Bright))
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1





