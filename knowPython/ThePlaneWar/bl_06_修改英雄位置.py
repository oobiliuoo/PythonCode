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

# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200, 500, 102, 126)
# 游戏循环
while True:
    # 设在刷新频率
    clock.tick(1)
    # 2.修改飞机的位置
    hero_rect.y -= 60
    # 3.调用blit方法绘制图像
    # 绘制背景覆盖原有图片
    screen.blit(bg, (0, 0))
    # 绘制飞机
    screen.blit(hero, hero_rect)
    # 4.调用update方法更新图像
    pygame.display.update()

    pass

pygame.quit()
