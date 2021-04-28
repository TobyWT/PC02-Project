import random
import tkinter


class Disk:
    def __init__(self, colour: str, player: int):
        self.colour = colour
        self.player = player

    def __str__(self) -> str:
        return self.colour


class ConnectFourGame:
    @staticmethod
    def create_disk_grid_copy(disk_grid):
        return [[disk for disk in row] for row in disk_grid]

    def check_for_win(self, col_number: int, disk_grid_copy, current_player: int) -> bool:
        # Find first Disk (from the top) for the dropped column
        row_index = 0
        while row_index < len(self.__disk_grid) - 1:
            if disk_grid_copy[row_index][col_number] is not None:
                break
            row_index += 1

        # Check three spaces horizontally/vertically/diagonally to see if they add up (individually) to >4
        vertical_count = 0
        diagonal_down = 0
        diagonal_up = 0

        # Create flags for when we stop counting horizontal/vertical/diagonal
        # (when there is another player's Disk in the way)

        stop_counting_vertical = False
        stop_counting_diagonal_down = False
        stop_counting_diagonal_up = False

        # Start with a counter going from 0 to 3 (for the three spaces after the Disk)
        for check in range(0, 4, 1):
            # Perform checks for vertical
            if 0 <= row_index + check < len(disk_grid_copy):
                if disk_grid_copy[row_index + check][col_number] is not None:
                    if (disk_grid_copy[row_index + check][col_number].colour
                            == self.__player_colours[current_player] and not stop_counting_vertical):
                        vertical_count += 1
                    else:
                        stop_counting_vertical = True
                else:
                    stop_counting_horizontal = True

            # Perform checks for diagonal down
            if (0 <= row_index + check < len(disk_grid_copy)
                    and (0 <= col_number + check < len(disk_grid_copy[row_index]))):
                if disk_grid_copy[row_index + check][col_number + check] is not None:
                    if (disk_grid_copy[row_index + check][col_number + check].colour
                            == self.__player_colours[current_player]) and not stop_counting_diagonal_down:
                        diagonal_down += 1
                    else:
                        stop_counting_diagonal_down = True
                else:
                    stop_counting_horizontal = True

            # Perform checks for diagonal up
            if (0 <= row_index - check < len(disk_grid_copy)
                    and (0 <= col_number + check < len(disk_grid_copy[row_index]))):
                if disk_grid_copy[row_index - check][col_number + check] is not None:
                    if (disk_grid_copy[row_index - check][col_number + check].colour
                            == self.__player_colours[current_player]) and not stop_counting_diagonal_up:
                        diagonal_up += 1
                    else:
                        stop_counting_diagonal_up = True
                else:
                    stop_counting_horizontal = True

        # Reset the flags for the opposite direction
        stop_counting_vertical = False
        stop_counting_diagonal_down = False
        stop_counting_diagonal_up = False

        # Start with a counter going from 0 to -3 (for the three spaces before the Disk)
        for check in range(-1, -4, -1):
            # Perform checks for vertical
            if 0 <= row_index + check < len(disk_grid_copy):
                if disk_grid_copy[row_index + check][col_number] is not None:
                    if (disk_grid_copy[row_index + check][col_number].colour
                            == self.__player_colours[current_player] and not stop_counting_vertical):
                        vertical_count += 1
                    else:
                        stop_counting_vertical = True
                else:
                    stop_counting_horizontal = True

            # Perform checks for diagonal down
            if (0 <= row_index + check < len(disk_grid_copy)
                    and (0 <= col_number + check < len(disk_grid_copy[row_index]))):
                if disk_grid_copy[row_index + check][col_number + check] is not None:
                    if (disk_grid_copy[row_index + check][col_number + check].colour
                            == self.__player_colours[current_player]) and not stop_counting_diagonal_down:
                        diagonal_down += 1
                    else:
                        stop_counting_diagonal_down = True
                else:
                    stop_counting_horizontal = True

            # Perform checks for diagonal up
            if (0 <= row_index - check < len(disk_grid_copy)
                    and (0 <= col_number + check < len(disk_grid_copy[row_index]))):
                if disk_grid_copy[row_index - check][col_number + check] is not None:
                    if (disk_grid_copy[row_index - check][col_number + check].colour
                            == self.__player_colours[current_player]) and not stop_counting_diagonal_up:
                        diagonal_up += 1
                    else:
                        stop_counting_diagonal_up = True
                else:
                    stop_counting_horizontal = True

        horizontal_count = 1
        for check in range(1, 4):
            # Check left side
            if 0 <= col_number - check:
                if disk_grid_copy[row_index][col_number - check] is not None:
                    if disk_grid_copy[row_index][col_number - check].player == current_player:
                        horizontal_count += 1
                    else:
                        break
                else:
                    break
            else:
                break
        for check in range(1, 4):
            # Check right side
            if col_number + check < len(disk_grid_copy[row_index]):
                if disk_grid_copy[row_index][col_number + check] is not None:
                    if disk_grid_copy[row_index][col_number + check].player == current_player:
                        horizontal_count += 1
                    else:
                        break
                else:
                    break
            else:
                break

        # Return True if any of these counters is >= 4
        return horizontal_count >= 4 or vertical_count >= 4 or diagonal_down >= 4 or diagonal_up >= 4

    def drop_disk(self, col_number: int, disk_grid_copy, current_player: int, prediction: bool) -> bool:
        # Don't perform the move if the col_number is not valid
        if col_number < 0 or col_number >= len(self.__disk_grid[0]):
            return False

        # Only drop a disk in the selected col_number if there is space
        if disk_grid_copy[0][col_number] is not None and not prediction:
            self.__message_label.config(text="Cannot place disk there (no room)!")
            self.__message_label.after(2000, lambda: self.__message_label.config(text="Message here..."))
            return False

        # Drop the correct player's disk in that position
        row_index = 1
        while row_index < len(disk_grid_copy):
            if disk_grid_copy[row_index][col_number] is not None:
                break
            row_index += 1
        row_index -= 1
        disk_grid_copy[row_index][col_number] = Disk(self.__player_colours[current_player], current_player)

        # Update the Canvas with the new disk
        if not prediction:
            self.__canvas.itemconfig(self.__oval_grid[row_index][col_number],
                                     fill=self.__player_colours[current_player])

        # Say we managed to place the player's Disk
        return True

    def min_max(self, current_depth: int, max_depth: int, disk_grid) -> [int]:
        pass

    def handle_turn(self, col_number: int) -> None:
        # Drop the player's Disk in the chosen column
        if self.drop_disk(col_number, self.__disk_grid, self.__current_player, False):
            # Check if the current player won
            if self.check_for_win(col_number, self.__disk_grid, self.__current_player):
                self.__message_label.config(text="Player {} Won!".format(self.__current_player))

            # Move on to the next player (the AI) - if we run min_max and get None, assume
            # it is a person controlling the game
            result = self.min_max(1, 3, self.__disk_grid)
            if result is None:
                self.__current_player = (self.__current_player + 1) % len(self.__player_colours)
            else:
                # Loop through the scores and choose the best column to place something in
                # (or a random position if there are only 0s)
                best_col_placement = 0
                best_score = -10
                for best_col_index in range(len(result)):
                    if result[best_col_index] is not None:
                        if result[best_col_index] > best_score:
                            best_score = result[best_col_index]
                            best_col_placement = best_col_index

                # If the best_score is unchanged, there are no more positions to drop a Disk onto
                if best_score == -10:
                    self.__message_label.config(text="THERE ARE NO MORE POSITIONS AVAILABLE")
                else:
                    # Otherwise, if it is 0 then there are no good positions to go to (so be random)
                    if best_score == 0:
                        positions_available = []
                        for col_index in range(len(result)):
                            if result[col_index] is not None:
                                if result[col_index] == 0:
                                    positions_available.append(col_index)
                        col_placement = random.choice(positions_available)
                    # Otherwise go to the best position
                    else:
                        col_placement = best_col_placement

                    # Place the disk at that position
                    self.drop_disk(col_placement, self.__disk_grid, self.__current_player + 1, False)

                    # Check if the AI won
                    if self.check_for_win(col_placement, self.__disk_grid, self.__current_player + 1):
                        self.__message_label.config(text="Player {} Won!".format(self.__current_player + 1))

    def __init__(self, circle_size: int):
        # The number of rows/columns in the grid (typically 6 rows by 7 columns)
        rows = 6
        cols = 7

        # Variables for the current player and the player's disk colours (0 = Red, 1 = Yellow)
        self.__current_player = 0
        self.__player_colours = ["#FF0000", "#FFFF00"]

        # Get the GUI setup for the game
        self.__window = tkinter.Tk()
        self.__window.title("Connect Four")
        self.__message_label = tkinter.Label(self.__window, text="Messages go here...", font=("Calibri", 26))
        self.__message_label.pack()
        self.__canvas = tkinter.Canvas(self.__window,
                                       width=(circle_size * cols), height=(circle_size * rows),
                                       bg="#FFFFFF")
        self.__canvas.bind("<Button-1>", lambda event: self.handle_turn(int(event.x / circle_size)))
        self.__canvas.pack()

        # Create the grid for the Disk objects
        self.__disk_grid = [[None for _ in range(cols)] for _ in range(rows)]

        # Create the grid for the ovals in the Canvas
        self.__oval_grid = [[self.__canvas.create_oval(col * circle_size, row * circle_size,
                                                       (col + 1) * circle_size, (row + 1) * circle_size,
                                                       fill="#FFFFFF") for col in range(cols)] for row in range(rows)]

        # Start the game
        self.__window.mainloop()


ConnectFourGame(50)
