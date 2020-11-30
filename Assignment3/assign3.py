def Search(array, value):
    """
    Binary search using while loop
    Question 1
    :param array: Sorted array to search
    :param value: Values we are searching
    :return: Returning the boolean value
    """
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == value:
            return True
        elif array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return False


def sortedHasSum(array, value):
    """
    Finding the pair of elements whose sum is the value
    Question 5a
    :param array: Sorted array in which we are searching
    :param value: Value to check
    :return: Returning boolean value
    """
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] == value:
            return True
        elif array[left] + array[right] < value:
            left += 1
        else:
            right -= 1
    return False


def hasSum(array, value):
    """
    Same function as above only no sorting done hence merge sort was used to meet the time complexity requirements
    Question 5b
    :param array: Unsorted array
    :param value: Value of the sum
    :return: Returning the boolean value
    """
    array = mergeSort(array)
    return sortedHasSum(array, value)


def mergeSort(array):
    """
    Merge sort
    :param array: Unsorted array
    :return: Returning the sorted array
    """
    if len(array) > 1:
        mid = len(array) // 2
        left = array[0: mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array


def quickSortforlogn(array, left, right):
    """
    To make the task easier in quick sort we are partitioning the array with the help of pivot index
    :param array: Unsorted array
    :param left: Leftmost value
    :param right: Rightmost value
    :return: Returning the pivot index for quick sort
    """
    pivot = array[right]
    pivotIndex = left - 1
    for i in range(left, right):
        if array[i] <= pivot:
            pivotIndex += 1
            array[pivotIndex], array[i] = array[i], array[pivotIndex]

    return pivotIndex


def quickSortHelp(array, left, right):
    """
    Quick sort helper function
    :param array: Unsorted array
    :param left: Leftmost value
    :param right: Rightmost value
    :return: Sorted array
    """
    while left < right:
        pivotIndex = quickSortforlogn(array, left, right)
        if pivotIndex - left < right - pivotIndex:
            quickSortHelp(array, left, pivotIndex - 1)
            left = pivotIndex + 1
        else:
            quickSortHelp(array, pivotIndex + 1, right)
            right = pivotIndex - 1

    return array


def quickSort(array):
    """
    Quicksort function calling the helper function
    Question 6
    :param array: Unsorted array
    :return: Returning the sorted array
    """
    return quickSortHelp(array, 0, len(array) - 1)


def main():
    array = [2, 3, 5, 8, 10, 13, 17, 18]
    array1 = [5, 4, 8, 2, 9, 10, 15, 70, 81]
    print(Search(array, 14))
    print(sortedHasSum(array, 20))
    print(hasSum(array1, 90))
    print(quickSort(array1))


if __name__ == '__main__':
    main()
