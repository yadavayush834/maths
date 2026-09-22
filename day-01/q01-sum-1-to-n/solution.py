"""Solution for Q01 — Sum 1 to n in O(1), no loop."""

import sys


def sum_1_to_n(n: int) -> int:
    """Return 1 + 2 + ... + n using the closed-form formula.

    Args:
        n: positive integer (n >= 0).

    Returns:
        n * (n + 1) // 2
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    # O(1) arithmetic series formula. No loop allowed.
    return n * (n + 1) // 2


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print(sum_1_to_n(n))


if __name__ == "__main__":
    solve()
