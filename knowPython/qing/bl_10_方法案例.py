class Game(object):
    top_score = 0

    def __init__(self, name):
        self.player_name = name

    @staticmethod
    def show_help():
        print("帮助信息：别让僵尸走进房间")

    @classmethod
    def show_top_score(cls):
        print("历史最高分：%d" % cls.top_score)

    def start_game(self):
        print("【%s】正在游戏" % self.player_name)

        Game.top_score = 999


jiangshi = Game("小明")
Game.show_help()
Game.show_top_score()
jiangshi.start_game()
Game.show_top_score()


