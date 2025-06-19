
def insertion_sort(arr):
    """
    Sorts an array using the insertion sort algorithm.

    The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are
    picked and placed at the correct position in the sorted part.

    Time complexity: O(n^2)
    Space complexity: O(1)

    Parameters
    ----------
    arr : list
        The array to be sorted

    Returns
    -------
    list
        The sorted array
    """
    for index in range(1, len(arr)):
        current_value = arr[index]
        position = index
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position = position - 1
        arr[position] = current_value
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(insertion_sort(arr))