"""Simple list utilities for practicing branching and merging."""

from __future__ import annotations


def chunk(items: list[int], size: int) -> list[list[int]]:
    if size <= 0:
        raise ValueError("size must be positive")
    return [items[i : i + size] for i in range(0, len(items), size)]


def flatten(nested: list[list[int]]) -> list[int]:
    result: list[int] = []
    for group in nested:
        result.extend(group)
    return result


def average(items: list[int]) -> float:
    if not items:
        raise ValueError("items cannot be empty")
    return sum(items) / len(items)


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7]
    groups = chunk(data, 3)
    print("Chunked:", groups)
    print("Flatten:", flatten(groups))
    print("Average:", average(data))
