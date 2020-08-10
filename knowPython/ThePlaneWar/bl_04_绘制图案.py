import pygame
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 加载图片
bg = pygame.image.load("./FJDZimages/background.png")

# 绘制图片
screen.blit(bg, (0, 0))

# 更新界面
pygame.display.update()

# 绘制英雄图像
hero = pygame.image.load("./FJDZimages/me1.png")
screen.blit(hero, (200, 500))
pygame.display.update()

# 游戏循环
while True:
    pass

pygame.quit()

