from typing import List


# 1. Bubble Sort
def bubble_sort(arr: List[int]) -> List[int]:
    """Многократно проходит по списку, меняя соседние элементы местами."""
    result = arr.copy()
    n = len(result)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


# 2. Selection Sort
def selection_sort(arr: List[int]) -> List[int]:
    """На каждом шаге находит минимум и ставит его в начало неотсортированной части."""
    result = arr.copy()
    n = len(result)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    return result


# 3. Insertion Sort
def insertion_sort(arr: List[int]) -> List[int]:
    """Постепенно строит отсортированную часть, вставляя элементы на нужное место."""
    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


# 4. Quick Sort
def quick_sort(arr: List[int]) -> List[int]:
    """Рекурсивно разбивает список относительно опорного элемента (pivot)."""
    if len(arr) <= 1:
        return arr.copy()
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# 5. Merge Sort
def merge_sort(arr: List[int]) -> List[int]:
    """Делит список пополам, сортирует половины и сливает их."""
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """Слияние двух отсортированных списков в один."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# 6. Heap Sort
def heap_sort(arr: List[int]) -> List[int]:
    """Строит max-кучу и последовательно извлекает максимум."""
    result = arr.copy()
    n = len(result)

    for i in range(n // 2 - 1, -1, -1):
        _sift_down(result, n, i)

    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]
        _sift_down(result, i, 0)

    return result


def _sift_down(arr: List[int], size: int, root: int) -> None:
    while True:
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < size and arr[left] > arr[largest]:
            largest = left
        if right < size and arr[right] > arr[largest]:
            largest = right

        if largest == root:
            break

        arr[root], arr[largest] = arr[largest], arr[root]
        root = largest


# тесты
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90, 5]

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort,
        "Heap Sort": heap_sort,
    }

    print(f"Исходный список: {data}\n")
    for name, func in algorithms.items():
        print(f"{name:15} -> {func(data)}")

    # проверка = реальный результат
    expected = sorted(data)
    assert all(func(data) == expected for func in algorithms.values())
    print("\n✅ Все алгоритмы дают корректный результат.")
