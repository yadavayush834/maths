# Q02 — Sum Multiples of k in [L, R]

## Problem Statement

Given `L`, `R` and `k`, find the sum of all numbers `x` such that:

```
L ≤ x ≤ R  and  x % k == 0
```

In words: add up all multiples of `k` lying inside the inclusive interval `[L, R]`.
If there is no such multiple, the answer is `0`.

You must not loop from `L` to `R`. Use an `O(1)` formula.

## Input

Single line with three integers:

```
L R k
```

## Output

Single integer — sum of all multiples of `k` in `[L, R]`.

## Constraints

- `1 ≤ L ≤ R ≤ 10⁹`
- `1 ≤ k ≤ 10⁹`
- `O(1)` time, `O(1)` space — no loop over the interval.
- Answer fits in 64-bit signed (`long long`). Max case `L=1, R=10⁹, k=1` gives `500000000500000000`.

## Examples

### Example 1
Input:
```
1 10 3
```
Output:
```
18
```
Explanation: `3 + 6 + 9 = 18`.

### Example 2
Input:
```
5 15 5
```
Output:
```
30
```
Explanation: `5 + 10 + 15 = 30`.

### Example 3
Input:
```
4 4 2
```
Output:
```
4
```

### Example 4
Input:
```
5 7 10
```
Output:
```
0
```
Explanation: no multiple of `10` in `[5, 7]`.

### Example 5
Input:
```
1 1000000000 1
```
Output:
```
500000000500000000
```

## Formula

Count of multiples of `k` up to `N`:

```
m = N / k   (floor)
sum_k(N) = k * (1 + 2 + ... + m) = k * m * (m + 1) / 2
```

Answer for interval:

```
ans = sum_k(R) - sum_k(L - 1)
```

where `a = R / k`, `b = (L - 1) / k`.

## Edge Cases

- Single element that is a multiple: `L = R = 4, k = 2 → 4`.
- Single element not a multiple: `L = R = 5, k = 2 → 0`.
- `k > R`: at most one multiple (only if `L ≤ ...` — mostly `0`).
- `k = 1`: sum of full interval = `R*(R+1)/2 - (L-1)*L/2`.
- Max values: `L = 1, R = 10⁹` — must use `long long`, not `int`.
