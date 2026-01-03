import tkinter as tk

def solve(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1, 10):
                    if valid(grid, i, j, n):
                        grid[i][j] = n
                        if solve(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True

def valid(grid, r, c, n):
    return n not in grid[r] and \
           all(grid[i][c] != n for i in range(9)) and \
           all(grid[r//3*3+i][c//3*3+j] != n for i in range(3) for j in range(3))

def run():
    grid = [[int(cells[i][j].get() or 0) for j in range(9)] for i in range(9)]
    solve(grid)
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(0, tk.END)
            cells[i][j].insert(0, grid[i][j])

root = tk.Tk()
root.title("Sudoku Solver")

cells = [[tk.Entry(root, width=2, font=("Arial", 14)) for j in range(9)] for i in range(9)]
for i in range(9):
    for j in range(9):
        cells[i][j].grid(row=i, column=j)

tk.Button(root, text="Solve", command=run).grid(row=9, column=0, columnspan=9)
root.mainloop()
