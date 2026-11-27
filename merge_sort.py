from typing import TypeVar

T = TypeVar("T")


def merge_sort(items: list[T]) -> list[T]:
    """Сортирует список по возрастанию методом слияния."""
    if len(items) <= 1:
        return items.copy()

    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    return _merge(left, right)


def _merge(left: list[T], right: list[T]) -> list[T]:
    result: list[T] = []
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
