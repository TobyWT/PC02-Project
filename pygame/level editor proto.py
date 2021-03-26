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
        self.gravity = False
        self.collision = False
        self.isJump = False

    def draw_player(self):
        pygame.draw.rect(window, self.colour, self.rect_info)


def draw_stuff():
    window.fill((0, 0, 0))
    mymap = open("MapInfo", "r")
    my_map_line1 = mymap.readline()
    my_map_info = tuple(my_map_line1)
    ob3 = pygame.Rect(my_map_info)
    pygame.draw.rect(window, (255, 0, 0), ob3)
    pygame.draw.rect(window, player1.colour, player1.rect_info)
    pygame.draw.rect(window, (0, 0, 255), ob1)
    pygame.draw.rect(window, (0, 0, 255), ob2)

    pygame.display.update()

"""
my_player_x = 400
my_player_y = 400
my_player_width = 400
my_player_height = 400"""

ob1 = pygame.Rect(100, 500, 600, 50)
ob2 = pygame.Rect(300, 300, 600, 50)
gravity_num = 2
player1 = Player(400, 200, 50, 50, (255, 0, 0))
jumpNum = 7
size_num = 0


def collide():
    if player1.rect_info.colliderect(ob1) or player1.rect_info.colliderect(ob2):
        player1.rect_info.y -= 1
        player1.collision = True
        player1.gravity = False

    else:
        player1.collision = False
        player1.gravity = True


def check_if_quit():
    global run_game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False


ball_move = True
run_game = True
while run_game:
    if player1.rect_info.y > 600:
        player1.rect_info.y = 200
        player1.rect_info.width = 50
        player1.rect_info.height = 50
        player1.rect_info.x = 300

        ob1.y = 500
        ob1.x = 100
        ob2.y = 300
        ob2.x = 500
        size_num = 0

    collide()
    draw_stuff()
    pygame.time.delay(30)
    user_input = pygame.key.get_pressed()
    if user_input[pygame.K_LEFT]:
        ob1.x += player1.vel
        ob2.x += player1.vel
    if user_input[pygame.K_RIGHT]:
        ob1.x -= player1.vel
        ob2.x -= player1.vel
    if user_input[pygame.K_UP]:
        if size_num < 10:
            player1.rect_info.width += 10
            player1.rect_info.height += 10
            player1.rect_info.x -= 10
            player1.rect_info.y -= 10
            size_num += 1

    if user_input[pygame.K_SPACE] and not player1.isJump and player1.collision:
        player1.isJump = True
        player1.gravity = False
    if player1.isJump:
        if jumpNum > 0:
            player1.rect_info.y -= (10 ** 2) * 0.5
            jumpNum -= 1
        else:
            player1.gravity = True
            jumpNum = 7
            player1.isJump = False

    if player1.gravity and not player1.collision:
        player1.rect_info.y += player1.vel * gravity_num
        collide()
    collide()

    check_if_quit()
pygame.quit()
