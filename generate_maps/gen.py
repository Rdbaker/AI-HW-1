import random
import csv


def create_map(num_rows, num_cols):
    random_grid = generate_random_grid(num_rows, num_cols)
    start = (random.randint(0, num_rows - 1), random.randint(0, num_cols - 1))
    goal = (random.randint(0, num_rows - 1), random.randint(0, num_cols - 1))
    while start == goal:
        print 'loooooooop'
        goal = (random.randint(0, num_rows - 1), random.randint(0, num_cols - 1))

    random_grid[start[0]][start[1]] = "S"
    random_grid[goal[0]][goal[1]] = "G"
    return random_grid


def generate_random_grid(num_rows, num_cols):
    return [[random.randint(1, 9) for _ in range(num_cols)] for i in range(num_rows)]


def write_grid_to_file(grid, fname):
    with open(fname, 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        for row in grid:
            writer.writerow(row)

if __name__ == "__main__":
    write_grid_to_file(create_map(5, 5), "test.grid")
