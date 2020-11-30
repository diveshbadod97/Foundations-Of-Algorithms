def max2(num1, num2):
    """
    A function to return the maximun of two numbers passed in it
    :param num1: First number
    :param num2: Second number
    :return: Max of the two is returned
    """
    maximum = num1 * bool(num1 // num2) + num2 * bool(num2 // num1)
    return maximum


def fSelect(list1, index):
    """
    This function returns the element present at the passed index after sorting the list
    :param list1: The list from which the element must be found
    :param index: Index of the element to be found is passed
    :return: Element present at the passed index is returned
    """
    if len(list1) == 0:
        return "Bad Index"
    else:
        l = []
        m = []
        s = []
        for i in range(len(list1)):
            if list1[i] < list1[0]:
                l.append(list1[i])
            elif list1[i] > list1[0]:
                m.append(list1[i])
            else:
                s.append(list1[i])
        if index < len(l):
            return fSelect(l, index)
        elif len(l) <= index < (len(l) + len(s)):
            return list1[0]
        else:
            return fSelect(m, index - (len(l) + len(s)))


def iPartitioning(array, left, right):
    """
    To make the task easier in quick sort we are partitioning the array with the help of pivot index
    :param array: Unsorted array
    :param left: Leftmost value
    :param right: Rightmost value
    :return: Returning the pivotIndex for selection
    """
    pivot = array[right]
    pivotIndex = left
    for i in range(left, right):
        if array[i] <= pivot:
            array[pivotIndex], array[i] = array[i], array[pivotIndex]
            pivotIndex += 1
    array[pivotIndex], array[right] = array[right], array[pivotIndex]
    return pivotIndex


def iSelectHelper(array, index, left, right):
    """
    Helper function for iSelect where actual implementation is applied
    :param array: Array from which the element is to be selected
    :param index: Index of the element is passed
    :param left: Leftmost part of the array
    :param right: Rightmost part of the array
    :return: Element at the index passed
    """
    if 0 <= index <= len(array):
        pivot = iPartitioning(array, left, right)
        if pivot == index:
            return array[pivot]
        elif pivot < index:
            return iSelectHelper(array, index, pivot + 1, right)
        else:
            return iSelectHelper(array, index, left, pivot - 1)


def iSelect(array, index):
    """
    iSelext function will return the element from the given index after sorting the array
    :param array: Array from which the element is to be selected
    :param index: Index of the element is passed
    :return: The element present the passed index is returned
    """
    return iSelectHelper(array, index, 0, len(array) - 1)


def main():
    list1 = [5, 1, 3, 2, 4]
    print("Maximum of two values without comparison:    " + str(max2(600, 200)))
    print("fSelect implementation for [5, 1, 3, 2, 4] at index 0:   " + str(fSelect(list1, 0)))
    print("fSelect implementation for [5, 1, 3, 2, 4] at index 4:   " + str(fSelect(list1, 4)))
    print("fSelect implementation for [5, 1, 3, 2, 4] at index 2:   " + str(fSelect(list1, 2)))
    print("iSelect implementation for [5, 1, 3, 2, 4] at index 0:   " + str(iSelect(list1, 0)))
    print("iSelect implementation for [5, 1, 3, 2, 4] at index 4:   " + str(iSelect(list1, 4)))
    print("iSelect implementation for [5, 1, 3, 2, 4] at index 2:   " + str(iSelect(list1, 2)))


if __name__ == '__main__':
    main()
