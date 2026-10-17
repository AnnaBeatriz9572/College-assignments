# Sudoku Solver 🧩

Hi everyone! 👋

This project started with a challenge from my professor. During class, we were watching a video from **Computerphile**, and he suggested that we try building our own Sudoku solver and see what we could improve along the way.

That challenge caught my attention, so I decided to give it a try! I built this project in Python using a Jupyter Notebook, working through the solving logic and adding checks to make sure the starting grid follows Sudoku rules.

## What does it do?

The program solves standard **9×9 Sudoku puzzles** using **recursive backtracking**. It tries possible numbers, explores where those choices lead, and goes back whenever it needs to try a different path.

Here’s how each part works!

## Step 1 — Representing the puzzle

The puzzle is stored in a variable called `grid`, which is a list containing nine other lists.

Each inner list represents a row, and each value represents a cell:

- Numbers from `1` to `9` are the clues already provided.
- `0` represents an empty cell that the solver needs to fill.

Throughout the code, `y` represents the row index, `x` represents the column index, and `n` is the number being tested.

## Step 2 — Checking the grid size

Before looking for a solution, `check_matrix()` checks whether the puzzle has:

- Exactly nine rows.
- Exactly nine values in every row.

This makes sure the solver receives the dimensions it expects before accessing individual cells.

## Step 3 — Checking whether a number fits

The function `possible(y, x, n)` checks whether the number `n` can be placed in an empty cell.

It checks three places:

1. **The row:** the number must not already appear in that row.
2. **The column:** the number must not already appear in that column.
3. **The 3×3 box:** the number must not already appear inside the same box.

To find where the box begins, the code uses:

```python
y0 = (y // 3) * 3
x0 = (x // 3) * 3
```

With indexes starting at zero, these calculations give the starting row and column of the box containing the cell.

If the number passes all three checks, the function returns `True`. Otherwise, it returns `False`.

## Step 4 — Validating the starting clues

Checking new candidates is only part of the job. The numbers already written in the puzzle also need to follow the rules!

The function `check_sudoku()` visits every cell and checks whether its value is an integer between `0` and `9`.

For each filled cell, it then:

1. Saves the original number.
2. Temporarily replaces it with `0`.
3. Calls `possible()` to check for conflicts.
4. Puts the original number back before continuing or returning `False`.

Temporarily removing the number matters because otherwise `possible()` would find that same number in its own cell and incorrectly treat it as a repetition.

The validation preserves the original clues, including when it finds an invalid puzzle.

## Step 5 — Searching for a solution

The `solve()` function first calls the validation functions.

If the grid is invalid, it prints an error message. Otherwise, it scans the grid until it finds an empty cell.

For that cell, it tries the numbers from `1` to `9`. Whenever `possible()` accepts a candidate, the solver places it in the grid and calls `solve()` again.

That recursive call continues the search with the newly filled cell in place.

## Step 6 — Going back and trying another path

A number can fit in the current cell and still lead to a dead end later.

When a recursive call finishes, this line clears the number that was being tested:

```python
grid[y][x] = 0
```

The solver can then try the next candidate.

This process is called **backtracking**: make a choice, explore the possibilities, undo the choice, and try another one.

## Step 7 — Displaying the results

When the solver reaches a grid without empty cells, it prints the completed puzzle using NumPy:

```python
print(np.matrix(grid))
```

The search then continues, so a puzzle with multiple solutions can produce multiple completed grids.

After the search finishes:

- `grid` returns to its original state.
- `solve()` returns `None`.
- If a valid puzzle has no solution, nothing is printed.

## Want to try it?

You’ll need **Python 3**, **NumPy**, and **Jupyter Notebook**.

Install the dependencies:

```bash
python -m pip install numpy notebook
```

Then open the notebook:

```bash
jupyter notebook resolvedor_sudoku.ipynb
```

Run the import cell, define your puzzle in `grid`, and run the function definition cells. Then call:

```python
solve()
```

To try another puzzle, assign it to `grid` and call `solve()` again.

## What I’m practicing

This project is a way to explore **recursion, backtracking, matrix traversal, and input validation**, starting from a challenge we discussed in class.

It also helped me understand why checking the initial input matters and how changing a value during validation requires carefully restoring it afterward.

Thanks for checking it out! Feel free to try the notebook with your own Sudoku puzzles. 🙂
