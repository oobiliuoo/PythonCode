import pygame
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 创建游戏时钟对象
clock = pygame.time.Clock()

# 加载图片
bg = pygame.image.load("./FJDZimages/background.png")

# 绘制图片
screen.blit(bg, (0, 0))

# 绘制英雄图像
hero = pygame.image.load("./FJDZimages/me1.png")
screen.blit(hero, (200, 500))

# 图片贴完后统一进行输出
pygame.display.update()

i = 0

# 游戏循环
while True:
    # 设在刷新频率
    clock.tick(60)
    print(i)
    i += 1
    pass

pygame.quit()
