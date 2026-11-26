# 1. Bubble Sort
def bubble_sort(arr: list[int]) -> list[int]:
    """Возвращает отсортированную копию arr (пузырьковая сортировка)."""
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
def selection_sort(arr: list[int]) -> list[int]:
    """Возвращает отсортированную копию arr (сортировка выбором)."""
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
def insertion_sort(arr: list[int]) -> list[int]:
    """Возвращает отсортированную копию arr (сортировка вставками)."""
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
def quick_sort(arr: list[int]) -> list[int]:
    """Возвращает отсортированную копию arr (быстрая сортировка)."""
    result = arr.copy()
    _quick_sort_range(result, 0, len(result) - 1)
    return result


def _quick_sort_range(arr: list[int], low: int, high: int) -> None:
    if low >= high:
        return
    pivot_idx = _partition(arr, low, high)
    _quick_sort_range(arr, low, pivot_idx - 1)
    _quick_sort_range(arr, pivot_idx + 1, high)


def _partition(arr: list[int], low: int, high: int) -> int:
    # схема Ломуто.
    mid = (low + high) // 2
    arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


# 5. Merge Sort
def merge_sort(arr: list[int]) -> list[int]:
    """Возвращает отсортированную копию arr (сортировка слиянием)."""
    result = arr.copy()
    if len(result) <= 1:
        return result
    buffer = [0] * len(result)
    _merge_sort_range(result, buffer, 0, len(result))
    return result


def _merge_sort_range(arr: list[int], buf: list[int], lo: int, hi: int) -> None:
    if hi - lo <= 1:
        return
    mid = (lo + hi) // 2
    _merge_sort_range(arr, buf, lo, mid)
    _merge_sort_range(arr, buf, mid, hi)
    _merge(arr, buf, lo, mid, hi)


def _merge(arr: list[int], buf: list[int], lo: int, mid: int, hi: int) -> None:
    i, j, k = lo, mid, lo
    while i < mid and j < hi:
        if arr[i] <= arr[j]:
            buf[k] = arr[i]
            i += 1
        else:
            buf[k] = arr[j]
            j += 1
        k += 1
    while i < mid:
        buf[k] = arr[i]
        i += 1
        k += 1
    while j < hi:
        buf[k] = arr[j]
        j += 1
        k += 1
    arr[lo:hi] = buf[lo:hi]


# 6. Heap Sort
def heap_sort(arr: list[int]) -> list[int]:
    """Возвращает отсортированную копию arr (пирамидальная сортировка)."""
    result = arr.copy()
    n = len(result)

    for i in range(n // 2 - 1, -1, -1):
        _sift_down(result, n, i)

    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]
        _sift_down(result, i, 0)

    return result


def _sift_down(arr: list[int], size: int, root: int) -> None:
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
ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Heap Sort": heap_sort,
}

EDGE_CASES: list[list[int]] = [
    [],                                # пустой
    [42],                              # один элемент
    [1, 1, 1, 1],                      # все равны
    [3, 1, 2, 3, 1, 2],                # дубликаты
    [-5, 0, -10, 5, 3],                # отрицательные и ноль
    list(range(10)),                   # уже отсортирован
    list(range(10, 0, -1)),            # обратный порядок
    [64, 34, 25, 12, 22, 11, 90, 5],   # смешанный
]


def _check_all() -> None:
    for name, func in ALGORITHMS.items():
        for original in EDGE_CASES:
            case = original.copy()
            expected = sorted(case)
            got = func(case)
            assert got == expected, f"{name} на {original}: {got} != {expected}"
            assert case == original, f"{name} изменил вход: {original} -> {case}"


def test_all_sorting_algorithms() -> None:
    _check_all()


def test_input_not_mutated() -> None:
    for func in ALGORITHMS.values():
        for original in EDGE_CASES:
            case = original.copy()
            func(case)
            assert case == original


if __name__ == "__main__":
    _check_all()
    print("Все алгоритмы корректны на граничных случаях, вход не мутируется.\n")

    data = [64, 34, 25, 12, 22, 11, 90, 5]
    print(f"Исходный список: {data}")
    for name, func in ALGORITHMS.items():
        print(f"{name:15} -> {func(data)}")
