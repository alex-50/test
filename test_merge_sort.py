import pytest
from merge_sort import merge_sort


@pytest.mark.parametrize(
    "input_data, expected",
    [
        pytest.param([], [], id="01_empty_list"),
        pytest.param([42], [42], id="02_single_element"),
        pytest.param([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], id="03_already_sorted"),
        pytest.param([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], id="04_reverse_sorted"),
        pytest.param([3, 1, 4, 5, 2], [1, 2, 3, 4, 5], id="05_unsorted_integers"),
        pytest.param([4, 2, 4, 1, 2, 1], [1, 1, 2, 2, 4, 4], id="06_duplicate_elements"),
        pytest.param([0, -10, 5, -3, 2, -1], [-10, -3, -1, 0, 2, 5], id="07_negative_and_zero"),
        pytest.param([3.14, 1.41, 2.71, 0.5], [0.5, 1.41, 2.71, 3.14], id="08_floats"),
        pytest.param(["banana", "apple", "cherry"], ["apple", "banana", "cherry"], id="09_strings"),
    ],
)
def test_merge_sort_cases(input_data, expected):
    assert merge_sort(input_data) == expected


def test_10_original_list_not_mutated():
    original = [3, 1, 2]
    result = merge_sort(original)

    assert result == [1, 2, 3]
    assert original == [3, 1, 2]
    assert result is not original
