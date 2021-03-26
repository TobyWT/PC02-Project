import pygame
import random
pygame.init()
window = pygame.display.set_mode((800, 600))


class Player:
    def __init__(self, x, y, width, height, colour):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect_info = pygame.Rect(self.x, self.y, self.width, self.height)
        self.vel = 10

    def draw_player(self):
        pygame.draw.rect(window, self.colour, self.rect_info)


class MyBall:
    def __init__(self, x, y, width, height, colour):
        self.random_trajectory = random.randint(0, 4)
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect_info = pygame.Rect(self.x, self.y, self.width, self.height)
        self.vel = 10
        self.traj_0 = False
        self.traj_1 = False
        self.traj_2 = False
        self.traj_3 = False
    """def __init__(self, x,  y, radius):
        self.trajectory = random.randint(0, 100)
        self.radius = radius
        self.x = x
        self.y = y

        self.vel = 10"""

    def draw_ball(self):
        # pygame.draw.circle(window, (0, 255, 0), (self.x, self.y), self.radius)
        pygame.draw.rect(window, self.colour, self.rect_info)


def collide():
    if paddle1.rect_info.colliderect(ball1.rect_info):
        ball1.vel *= -1
    if paddle2.rect_info.colliderect(ball1.rect_info):
        ball1.vel *= -1
    if ball1.rect_info.y > 595 or ball1.rect_info.y < 5:
        ball1.vel *= -1


def draw_stuff():
    window.fill((0, 0, 0))
    paddle1.draw_player()
    paddle2.draw_player()
    ball1.draw_ball()
    pygame.display.update()


def check_if_quit():
    global run_game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False


ball_move = True
ball1 = MyBall(400, 300, 20, 20, (0, 255, 0))
paddle1 = Player(20, 300, 50, 130, (255, 0, 0))
paddle2 = Player(730, 300, 50, 130, (0, 0, 255))
rect1 = paddle1.rect_info
run_game = True
while run_game:
    collide()
    draw_stuff()
    pygame.time.delay(30)
    user_input = pygame.key.get_pressed()
    if user_input[pygame.K_DOWN]:
        paddle2.rect_info.y += paddle2.vel
    if user_input[pygame.K_UP]:
        paddle2.rect_info.y -= paddle2.vel
    if user_input[pygame.K_w]:
        paddle1.rect_info.y -= paddle1.vel
    if user_input[pygame.K_s]:
        paddle1.rect_info.y += paddle1.vel
    if user_input[pygame.K_d]:
        paddle1.rect_info.x += paddle1.vel
    if user_input[pygame.K_a]:
        paddle1.rect_info.x -= paddle1.vel

    check_if_quit()
pygame.quit()
