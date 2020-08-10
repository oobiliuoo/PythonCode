#!/usr/bin/python3.8
import pygame
from plone_sprite import *


class PloneGame(object):

    def __init__(self):
        print("初始化...")

        # 1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3.创建精灵和精灵组
        self.__create_sprite()

        # 设置定时器事件 -- 创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 设在定时器事件 -- 发射子弹 0.5s
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprite(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始")
        while True:
            # 1.设在刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵
            self.__update_sprites()
            # 5.更新显示
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():
            # 判断是否退出
            if event.type == pygame.QUIT:
                PloneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场...")
                # 创建敌机精灵
                enemy = Enemy()
                # 创建敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.type == pygame.K_RIGHT:
            #     print("英雄向右移动...")

        # 返回所有按键的元组，如果某个键被按下，对应的值会是1
        key_pressed = pygame.key.get_pressed()
        # 判断是否按下了方向键
        if key_pressed[pygame.K_RIGHT]:
            print("向右运动。。。")
            self.hero.speed = 3
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 1.子弹销毁敌机
        pygame.sprite.groupcollide(self.hero.bulltes, self.enemy_group, True, True)
        # 2.敌机摧毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies):
            # 英雄牺牲
            self.hero.kill()
            # 结束游戏
            PloneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bulltes.update()
        self.hero.bulltes.draw(self.screen)

    @staticmethod
    def __game_over():
        print("得分：%d" % PloneGame.count)
        print("---- 游戏结束 ----")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PloneGame()

    # 启动游戏
    game.start_game()
