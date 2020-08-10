import random
import pygame


# 创建屏幕常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 定义刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战精灵"""
    def __init__(self, image_name, speed=1):
        # 调用父类初始化
        super().__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    """背景精灵"""
    def __init__(self, is_alt=False):
        """
        :param is_alt: 判断是否为交替图像
        """
        # 调用父类创建精灵，设置属性
        super().__init__("./FJDZimages/background.png")
        # 判断是否是交替图像，如果是，进需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类实现
        super().update()
        # 判断是否移出屏幕， 如果是，将图像设在屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        # 1.调用父类方法，创建敌机，并且指定敌机图片
        super().__init__("./FJDZimages/enemy1.png")
        # 2.指定敌机的初始随机数度
        self.speed = random.randint(1, 3)
        # 3.指定敌机的初始随机位置
        # bottom = y - height
        self.rect.bottom = 0
        # max_x 敌机能出现的表示最右边位置
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)


    def update(self):
        # 1.调用父类，保持垂直方向飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是，从精灵组删除
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出高度，需要删除...")
            # kill方法可以将精灵从所有精灵组中移除,精灵就会被自动销毁
            self.kill()

    def __del__(self):
        # print("敌机挂了...%s" % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        # 1.调用父类，设置图片和速度
        super().__init__("./FJDZimages/me1.png", 0)
        # 2.设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹精灵组
        self.bulltes = pygame.sprite.Group()


    def update(self):
        self.rect.x += self.speed

        # 控制英雄不能超出屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹...")
        for i in range(0, 3):
            # 1.创建子弹精灵
            bullet = Bullet()
            # 2.设置子弹位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 3.添加到精灵组
            self.bulltes.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        super().__init__("./FJDZimages/bullet1.png", -2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁")