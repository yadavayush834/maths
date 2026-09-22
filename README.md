# Maths — Daily Practice

Daily maths / problem-solving practice. Questions are added day-wise.

## Structure

```
maths/
  README.md
  day-01/
    q01-<slug>/
      question.md    # full problem statement
      solution.py    # solution
      testcases.py   # test cases (runnable)
    q02-<slug>/
      ...
  day-02/
    ...
```

- Each day gets a folder: `day-01/`, `day-02/`, ...
- Each question gets its own folder: `q01-...`, `q02-...` (numbering continues per day, or globally — keep per-day for simplicity).
- Inside each question folder there are always 3 files:
  1. `question.md`
  2. `testcases.py`
  3. `solution.py`

## How to run a question

```bash
cd day-01/q01-sum-1-to-n
python3 solution.py          # reads n from stdin, prints answer
python3 testcases.py         # runs all test cases against solution.py
```

## Progress log

| Day | Date | Questions |
|-----|------|-----------|
| day-01 | 2026-09-22 | q01-sum-1-to-n: Sum all integers from 1 to n (n ≤ 10⁹, no loop) |

## Workflow

1. Give a short description / intro of the question.
2. I expand it into a full `question.md`, add `testcases.py` and `solution.py` in a new `day-XX/qYY-...` folder.
3. Everything is committed and pushed day-wise.
