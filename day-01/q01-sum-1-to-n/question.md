# Q01 — Sum All Integers from 1 to n (Without a Loop)

## Problem Statement

Given a positive integer `n`, compute the sum of all integers from `1` to `n` inclusive:

```
S(n) = 1 + 2 + 3 + ... + n
```

You **must not** use a loop (no `for`, `while`, or recursion that iterates n times).
Your solution must run in `O(1)` time and `O(1)` space, even for the maximum constraint.

This is the classic Gauss sum / arithmetic series problem.

## Input

- A single integer `n`.

## Output

- A single integer: the sum `1 + 2 + ... + n`.

## Constraints

- `1 ≤ n ≤ 10⁹`
- Time complexity must be `O(1)` — a loop up to `n` will TLE / time out for `n = 10⁹`.
- Space complexity: `O(1)`.
- Do not use loops. Use the closed-form formula.
- The answer for `n = 10⁹` is `500000000500000000`, which fits in 64-bit signed integer (`< 2⁶³-1 ≈ 9.22 × 10¹⁸`). In Python ints are arbitrary precision anyway.

## Examples

### Example 1
Input:
```
5
```
Output:
```
15
```
Explanation: `1 + 2 + 3 + 4 + 5 = 15`.

### Example 2
Input:
```
1
```
Output:
```
1
```

### Example 3
Input:
```
10
```
Output:
```
55
```

### Example 4
Input:
```
1000000000
```
Output:
```
500000000500000000
```

## Formula

Arithmetic series sum:

```
S(n) = n * (n + 1) / 2
```

Use integer arithmetic: `n * (n + 1) // 2`.

Why it works: pair the first and last terms `(1 + n)`, `(2 + (n-1))`, ... — there are `n/2` such pairs, each summing to `n + 1`.

## Edge Cases to Consider

- `n = 1` → `1`
- `n = 2` → `3`
- Large `n = 10⁹` → must not loop, must not overflow in languages with fixed-width ints (use 64-bit).
- If your implementation accepts `n = 0`, the correct sum is `0` (empty / base case), though the constraints say `n ≥ 1`.

## Follow-up

- Prove the formula by induction.
- What if you must sum from `l` to `r` inclusive? Answer: `S(r) - S(l-1)`.
