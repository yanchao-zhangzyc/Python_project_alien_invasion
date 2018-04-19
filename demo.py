import sys
import pygame
from ship import Ship
from setting import Settings
import game_functions as gf
'''初始化游戏，创建一个屏幕对象'''
def run_game():
    pygame.init()#游戏程序初始化
    ai_setting=Settings()
    screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_width))#创建显示屏窗口大小
    pygame.display.set_caption("Alien Invasion")#设置游戏名称
    ship=Ship(screen)#//创建一艘飞船

    #开始游戏的主循环
    '''检测到事件类型为quit时，退出游戏'''
    while True:
        #监视键盘和鼠标事件
        gf.check_events()
        #绘制屏幕
        screen.fill(ai_setting.bg_color)
        ship.blitme()#绘制飞船
        #让绘制的屏幕可见
        pygame.display.flip()
run_game()