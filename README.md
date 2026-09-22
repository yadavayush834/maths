# Maths — Daily Practice

Daily maths / problem-solving practice. Questions are added day-wise.

## Structure

```
maths/
  README.md
  day-01/
    q01-<slug>/
      question.md    # full problem statement
      sol.cpp        # simple solution (short names)
      tc.txt         # testcases (input -> output)
    q02-<slug>/
      ...
  day-02/
    ...
```

- Each day gets a folder: `day-01/`, `day-02/`, ...
- Each question gets its own folder: `q01-...`, `q02-...` (numbering continues per day, or globally — keep per-day for simplicity).
- Inside each question folder there are always 3 files:
  1. `question.md`
  2. `tc.txt`
  3. `sol.cpp`

## How to run a question

```bash
cd day-01/q01-sum-1-to-n
g++ -O2 -std=c++17 sol.cpp -o sol
echo 5 | ./sol          # 15
```

Check testcases in `tc.txt` (`input -> output`).

## Progress log

| Day | Date | Questions |
|-----|------|-----------|
| day-01 | 2026-09-22 | q01-sum-1-to-n: Sum all integers from 1 to n (n ≤ 10⁹, no loop), q02-sum-multiples-k-interval: Sum multiples of k in [L, R] |

## Workflow

1. Give a short description / intro of the question.
2. I expand it into a full `question.md`, add `tc.txt` and `sol.cpp` in a new `day-XX/qYY-...` folder.
3. Each file is committed + pushed one-by-one (more commits).
