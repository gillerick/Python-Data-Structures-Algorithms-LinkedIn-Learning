def read_maze(file_name):
    """
    :param File containing the maze to be read:
    :return: a 2-Dimensional list containing the maze representation

    """

    try:
        with open(file_name) as fh:
            maze = [[char for char in line.strip("\n")] for line in fh]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print("The maze is not rectangular")
                    raise SystemExit
            return maze
    except OSError:
        print("There is a problem with the selected file")
        raise SystemExit


if __name__== '__main__':
    maze = read_maze("Mazes/pacman_maze.txt")
    for row in maze:
        print(row)

    print("\n-----------------------------\n")

    maze = read_maze("Mazes/mini_maze_dfs.txt")
    for row in maze:
        print(row)
