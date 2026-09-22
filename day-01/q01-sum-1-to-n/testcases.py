"""Test cases for Q01 — Sum 1 to n.

Run with:
    python3 testcases.py
"""

from solution import sum_1_to_n

# (input_n, expected_output)
TEST_CASES = [
    (1, 1),                       # minimal input
    (2, 3),                       # 1 + 2
    (5, 15),                      # example 1
    (10, 55),                     # example 3
    (100, 5050),                  # classic Gauss: 1..100
    (1000, 500500),
    (1000000, 500000500000),      # 10^6
    (1000000000, 500000000500000000),  # max constraint n = 10^9
    (0, 0),                       # robustness: empty sum
    (999999999, 499999999500000000),  # just below max
]


def run_tests() -> None:
    passed = 0
    for i, (n, expected) in enumerate(TEST_CASES, start=1):
        got = sum_1_to_n(n)
        status = "PASS" if got == expected else "FAIL"
        if status == "PASS":
            passed += 1
        print(f"Test {i:02d}: n={n:<12} expected={expected:<20} got={got:<20} [{status}]")
        assert got == expected, f"Test {i} failed: n={n}, expected {expected}, got {got}"
    print(f"\n{passed}/{len(TEST_CASES)} tests passed.")


if __name__ == "__main__":
    run_tests()
