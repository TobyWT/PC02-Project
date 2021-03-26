import math
import random
import tkinter


class PongPaddle:
    """
    A class for a single paddle in the game of Pong
    """
    def __init__(self, canvas: tkinter.Canvas, position: (int, int), size: (int, int)):
        """
        Constructs the paddle. Has the following instance variables
        :var self.__canvas_reference: A reference to the canvas (so it can move the paddle up/down)
        :var self.__position_x: The X position of the paddle
        :var self.__position_y: The Y position of the paddle
        :var self.__size_width: The width (horizontal size) of the paddle
        :var self.__size_length: The length (vertical size) of the paddle
        :var self.__vertical_direction: The direction the paddle is moving in (1 = downwards, 0 = still, -1 = upwards)
        :var self.__speed: The speed of the paddle's movement (integer based, so too slow will stop it moving)
        :param canvas: The canvas of the program
        :param position: The starting position of the paddle
        :param size: The size of the paddle
        """
        self.__canvas_reference = canvas
        self.__position_x, self.__position_y = position
        self.__size_width, self.__size_length = size
        # Create a rectangle in the canvas for the paddle
        self.__paddle_reference = self.__canvas_reference.create_rectangle(
            self.__position_x,
            self.__position_y,
            self.__position_x + self.__size_width,
            self.__position_y + self.__size_length,
            fill="#FF0000"
        )
        self.__vertical_direction = 0
        self.__speed = 150

    def update(self, dt: int) -> None:
        """
        Updates the paddle every 'tick' in the game (default is 16ms, roughly 60FPS)
        Used for moving the paddle
        :param dt: The time since the previous update (in ms)
        """
        distance = int(self.__vertical_direction * self.__speed * dt * 0.001)
        self.__position_y += distance
        self.__canvas_reference.move(self.__paddle_reference, 0, distance)

    def move_up(self):
        """
        Starts moving the paddle upwards
        """
        self.__vertical_direction = -1

    def move_down(self):
        """
        Starts moving the paddle downwards
        """
        self.__vertical_direction = 1

    def stop_moving(self):
        """
        Stops the paddle moving
        """
        self.__vertical_direction = 0

    def get_bounds(self) -> (int, int, int, int):
        """
        Gets the pixel bounds of the paddle (in the order of left, top, right, bottom)
        :return: The bounds of the paddle
        """
        return (
            self.__position_x,
            self.__position_y,
            self.__position_x + self.__size_width,
            self.__position_y + self.__size_length
        )


class PongBall:
    """
    A class for the ball in the game of Pong
    """
    def __init__(self, canvas: tkinter.Canvas, position: (int, int), size: int):
        """
        Constructs the ball. Has the following instance variables
        :var self.__canvas_reference: A reference to the canvas (so it can move the ball up/down)
        :var self.__position_x: The X position of the ball
        :var self.__position_y: The Y position of the ball
        :var self.__size: The size of the ball
        :var self.__direction: The direction the ball is going in (X, Y)
        :var self.__speed: The speed of the ball (integer based, so too slow will stop it moving)
        :param canvas: The canvas of the program
        :param position: The starting position of the ball
        :param size: The size of the ball
        """
        self.__canvas_reference = canvas
        self.__position_x, self.__position_y = position
        self.__size = size
        self.__ball_reference = self.__canvas_reference.create_oval(
            self.__position_x,
            self.__position_y,
            self.__position_x + self.__size,
            self.__position_y + self.__size,
            fill="#FFFF00"
        )
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.__direction = random.choice(directions)
        self.__speed = 200

    def get_canvas_id(self):
        """
        Returns the ball's canvas ID (for deletion if it goes off screen)
        :return: The ID of the ball
        """
        return self.__ball_reference

    def update(self, dt: int) -> None:
        """
        Updates the ball every 'tick' in the game (default is 16ms, roughly 60FPS)
        Used for moving the ball
        :param dt: The time since the previous update (in ms)
        """
        magnitude = math.sqrt((self.__direction[0] ** 2) + (self.__direction[1] ** 2))
        pixel_distance = (
            self.__direction[0] * self.__speed * dt * 0.001 / magnitude,
            self.__direction[1] * self.__speed * dt * 0.001 / magnitude
        )
        self.__position_x += int(pixel_distance[0])
        self.__position_y += int(pixel_distance[1])
        self.__canvas_reference.move(self.__ball_reference, int(pixel_distance[0]), int(pixel_distance[1]))

    def reverse_direction(self, x: bool, y: bool) -> None:
        """
        Flips the direction of the ball in the X or Y axis
        :param x: Whether to flip in the X axis
        :param y: Whether to flip in the Y axis
        """
        self.__direction = (
            self.__direction[0] * (-1 if x else 1),
            self.__direction[1] * (-1 if y else 1)
        )

    def get_bounds(self) -> (int, int, int, int):
        """
        Gets the pixel bounds of the ball (in the order of left, top, right, bottom)
        :return: The bounds of the ball
        """
        return (
            self.__position_x,
            self.__position_y,
            self.__position_x + self.__size,
            self.__position_y + self.__size
        )


class PongGame:
    """
    A class representing the entire game of Pong
    """
    def __init__(self, canvas_size: (int, int)):
        """
        Constructs a game of Pong and sets up the paddles and ball. Has the following instance variables:
        :var self.__canvas_size: The size of the canvas (used for checking if the ball goes off screen)
        :var self.__window: The tkinter Window
        :var self.__canvas: The tkinter Canvas
        :var self.__paddle_1: The left paddle (Player 1)
        :var self.__paddle_2: The right paddle (Player 2)
        :var self.__ball: The ball
        :param canvas_size: The size of the canvas
        """
        self.__canvas_size = canvas_size
        self.__window = tkinter.Tk()
        self.__window.title("Pong")
        self.__canvas = tkinter.Canvas(self.__window, width=canvas_size[0], height=canvas_size[1], bg="#333333")
        self.__canvas.pack()
        self.__paddle_1 = PongPaddle(self.__canvas, (40, int((canvas_size[1] // 2) - 50)), (20, 100))
        self.__paddle_2 = PongPaddle(self.__canvas, (canvas_size[0] - 60, int((canvas_size[1] // 2) - 50)), (20, 100))
        self.__ball = PongBall(self.__canvas, (395, 245), 10)

    def reset_ball(self, paddle_winner: int) -> None:
        """
        Resets the ball's position to the middle of the screen (in fact, destroys the old ball and makes a new one)
        :param paddle_winner: The winner of that 'round' (1 for Player 1/left paddle and 2 for Player 2/right paddle)
        """
        self.__canvas.delete(self.__ball.get_canvas_id())
        self.__ball = PongBall(self.__canvas, (395, 245), 10)
        if paddle_winner == 1:
            pass
        elif paddle_winner == 2:
            pass

    def update(self) -> None:
        """
        Updates the game every 'tick'
        Used for moving the paddles, ball, and detecting collisions
        """
        # Update the paddles and ball so they move
        self.__paddle_1.update(16)
        self.__paddle_2.update(16)
        self.__ball.update(16)

        # Detect if the ball has collided with the top/bottom or either of the paddles (and reverse direction appropriately)
        ball_bounds = self.__ball.get_bounds()
        paddle_bounds = [self.__paddle_1.get_bounds(), self.__paddle_2.get_bounds()]
        if ball_bounds[1] <= 0 or ball_bounds[3] >= self.__canvas_size[1]:
            self.__ball.reverse_direction(False, True)
        for paddle_bound in paddle_bounds:
            if (ball_bounds[0] <= paddle_bound[2] and ball_bounds[2] >= paddle_bound[0]
                    and ball_bounds[1] <= paddle_bound[3] and ball_bounds[3] >= paddle_bound[1]):
                self.__ball.reverse_direction(True, False)

        # Detect if the ball has gone off the left/right side of the screen (and reset the ball using the correct player as the winner)
        if ball_bounds[2] <= 0:
            self.reset_ball(2)
        if ball_bounds[0] >= self.__canvas_size[0]:
            self.reset_ball(1)

        # Run this update function again after 16ms (roughly 60FPS)
        self.__window.after(16, self.update)

    def start(self) -> None:
        """
        Starts the game (and sets up the update function to run after 16ms)
        """
        self.__window.after(16, self.update)
        self.__window.mainloop()


# Instantiate the game and start it
game = PongGame((800, 400))
game.start()
