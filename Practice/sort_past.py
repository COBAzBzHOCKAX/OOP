import random

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

def sort_past(array):
    count = 0
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0:
            count += 1
            if (array[idx - 1] <= x):
                break
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x


def sort(array_left, array_right):
    print(array_left, array_right)
    result = []
    a = 0
    for i in range(len(array_left)):
        for j in range(a, len(array_right)):
            if array_left[i] < array_right[j]:
                break
            else:
                result.append(array_right[j])
                a = j + 1
        result.append(array_left[i])
    if a <= len(array_right) - 1:
        result.extend(array_right[a:])
    return result

def sort_delenie(array):
    if len(array) // 2:
        array_left = sort_delenie(array[:len(array)//2])
        array_right = sort_delenie(array[len(array)//2:])
        return sort(array_left, array_right)
    else:
        return array

# print(sort_delenie(array))


def qsort(array, left, right):
    p = random.choice(array[left:right+1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


arr = [2, 3, 1, 4, 6, 5, 9, 8, 7]
qsort(arr, 0, len(arr)-1)
print(arr)