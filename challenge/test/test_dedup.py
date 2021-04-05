from typing import Dict, List
import pytest

from code_challenge import dedup


@pytest.mark.parametrize(
    "test_input,expected_result",
    [
        ((1, 2, 3, 4, 5, 3, 3), (1, 2, 3, 4, 5)),
        ((2, 3, 4, 5, 1, 3, 3), (1, 2, 3, 4, 5)),
    ],
)
def test_dedup_int(test_input, expected_result):
    """Test int deduplication."""
    test_out = dedup.dedup_ints(test_input)
    assert isinstance(test_out, tuple)
    assert all(isinstance(i, int) for i in test_out)
    assert test_out == expected_result


@pytest.mark.parametrize(
    "test_input,expected_result",
    [
        (
            [{"a": 1, "b": 3}, {"a": 1, "b": 3}, {"a": 2, "b": 6}],
            [{"a": 1, "b": 3}, {"a": 2, "b": 6}],
        ),
        (
            [{"a": 1, "b": 3}, {"a": 2, "b": 6}, {"a": 1, "b": 3}],
            [{"a": 2, "b": 6}, {"a": 1, "b": 3}],
        ),
    ],
)
def test_dedup_dict(test_input, expected_result):
    """Test deduplication of list of dicts on all keys."""
    test_out = dedup.dedup_dicts(test_input)
    assert isinstance(test_out, list)
    assert all(isinstance(i, dict) for i in test_out)
    assert _sort_list_of_dicts(test_out) == _sort_list_of_dicts(expected_result)


@pytest.mark.parametrize(
    "test_input,expected_result",
    [
        (
            [
                {"a": 1, "b": 3, "c": 4},
                {"a": 1, "b": 3, "c": 4},
                {"a": 1, "b": 3, "c": 5},
            ],
            [{"a": 1, "b": 3, "c": 4}],
        )
    ],
)
def test_dedup_on_key(test_input, expected_result):
    """Test deduplication on select keys."""
    test_out = dedup.dedup_dicts_on_key(test_input, ("a", "b"))
    assert isinstance(test_out, list)
    assert all(isinstance(i, dict) for i in test_out)
    assert _sort_list_of_dicts(test_out) == _sort_list_of_dicts(expected_result)


def _sort_list_of_dicts(list_of_dicts: List[Dict]) -> List[Dict]:
    """Sort list of dicts by ascending keys within each dict, and by ascending
    values across dicts."""
    # Sort every dict by ascending keys
    test_out_sorted = [dict(sorted(e.items())) for e in list_of_dicts]
    # Sort by ascending values of the dicts
    return sorted(test_out_sorted, key=lambda x: tuple(x.values()))
