def bubbleSort(arr):
    """
    Sorts an array using bubble sort algorithm.

    Bubble sort, also known as sinking sort, is a simple sorting algorithm that works
    by repeatedly swapping adjacent elements if they are in the wrong order.

    The algorithm gets its name from the way smaller elements "bubble" to the top of
    the list.

    Time complexity: O(n^2)
    Space complexity: O(1)

    :param arr: array to be sorted
    :return: sorted array 
    """
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(bubbleSort(arr))  
