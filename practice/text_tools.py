"""String helper functions for Git practice edits."""

from __future__ import annotations


def word_count(text: str) -> int:
    return len(text.split())


def unique_words(text: str) -> set[str]:
    return {word.lower() for word in text.split()}


def reverse_lines(text: str) -> str:
    lines = text.splitlines()
    return "\n".join(reversed(lines))


if __name__ == "__main__":
    sample = "Git makes version control fun and powerful"
    print("Words:", word_count(sample))
    print("Unique:", sorted(unique_words(sample)))
    print("Reverse:\n" + reverse_lines(sample))
    
