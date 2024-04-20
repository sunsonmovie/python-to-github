import pygame
import sys
import random

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 设置蛇的初始位置
snake_pos = [[100, 100], [80, 100], [60, 100]]

# 设置食物的初始位置
food_pos = [300, 300]

# 设置蛇的初始速度
snake_speed = [20, 0]

# 设置游戏时钟
clock = pygame.time.Clock()

while True:
    # 检测按键事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_speed = [0, -20]
            elif event.key == pygame.K_DOWN:
                snake_speed = [0, 20]
            elif event.key == pygame.K_LEFT:
                snake_speed = [-20, 0]
            elif event.key == pygame.K_RIGHT:
                snake_speed = [20, 0]

    # 更新蛇的位置
    snake_pos.insert(0, [snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]])

    # 检测蛇是否吃到食物
    if snake_pos[0] == food_pos:
        food_pos = [random.randrange(1, screen_width // 20) * 20, random.randrange(1, screen_height // 20) * 20]
    else:
        snake_pos.pop()

    # 检测蛇是否撞到自己或者墙壁
    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= screen_width or
            snake_pos[0][1] < 0 or snake_pos[0][1] >= screen_height or
            snake_pos[0] in snake_pos[1:]):
        pygame.quit()
        sys.exit()

    # 更新游戏界面
    screen.fill(black)
    for pos in snake_pos:
        pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], 20, 20))
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 20, 20))
    pygame.display.flip()

    # 控制游戏速度
    clock.tick(10)
