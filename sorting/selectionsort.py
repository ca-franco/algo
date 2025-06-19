
def selectionSort(arr):
    """
    Sorts an array using the selection sort algorithm.

    Selection sort is an in-place comparison sorting algorithm. It has a time complexity of O(n^2)
    in the worst case, making it inefficient on large lists. It is mainly used for educational
    purposes to introduce the concept of sorting algorithms.

    The algorithm works by repeatedly swapping the minimum element from the unsorted part of the
    list with the first element of the unsorted part.

    :param arr: array to be sorted
    :return: sorted array
    """
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(selectionSort(arr))