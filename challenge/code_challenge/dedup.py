"""Deduplication of various data types."""
from typing import Dict, List, Tuple


def dedup_ints(list_of_ints: Tuple[int]) -> Tuple[int]:
    """Deduplicate and sort integers by ascending value."""
    
    return tuple([item for index, item in enumerate(list_of_ints) if item not in list_of_ints[:index]].sort())


def dedup_dicts(list_of_dicts: List[Dict]) -> List[Dict]:
    """Deduplicate a list of dicts.

    Two dicts are considered equal if all of their keys and values match.
    """
    return [dict(t) for t in set(tuple(d.items) for d in list_of_dicts)]
    


def dedup_dicts_on_key(list_of_dicts: List[Dict], dedup_on: List[str]) -> List[Dict]:
    """Deduplicate a list of dicts on a subset of keys only.

    Dicts should only be considered equivalent if their values for all keys in
    the argument `dedup_on` match. If dicts in the list need be deduplicated, the
    first dict in the list `list_of_dicts` should be kept.
    """
    pass
