# LeetCode Python

My personal repository for practicing algorithms, data structures, and problem-solving using Python.

## Goal

Not just to accumulate solved problems, but to learn how to:

- recognize algorithmic patterns;
- choose appropriate data structures;
- analyze time and space complexity;
- write clean, testable Python code;
- use Git regularly.

## Structure

- `solutions/` — solutions to LeetCode problems, organized by topic and difficulty.
- `tests/` — local tests using pytest.
- `patterns/` — reusable templates and implementations of key patterns.
- `notes/` — personal notes and explanations.

## Workflow

1. I read the problem.
2. I try to solve it on my own for 20–30 minutes.
3. If I get stuck, I look for a hint.
4. I implement the solution.
5. I record the `Time` and `Space` metrics.
6. I add at least one local test.
7. I document the pattern.
8. After a few days, I try to solve it again without looking at my code.

## Execution

Create a virtual environment and install the project:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Then:

```bash
python -m pip install -e .
pytest
```

## Personal Status

- 🟢 Solved — solved on my own
- 🟡 Review — solved, but needs to be reviewed
- 🔴 Struggle — not yet solved on my own
- 🔵 Mastered — pattern mastered