"""A tiny calculator module for practicing Git staging."""

from __future__ import annotations


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("add(2, 3) ->", add(2, 3))
    print("subtract(10, 4) ->", subtract(10, 4))
    print("multiply(6, 7) ->", multiply(6, 7))
    print("divide(5, 2) ->", divide(5, 2))
    print("Hello Calculator!")
