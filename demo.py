import sys
import pygame
'''初始化游戏，创建一个屏幕对象'''
def run_game():
    pygame.init()#游戏程序初始化
    screen=pygame.display.set_mode((1200,600))#创建显示屏窗口大小
    pygame.display.set_caption("Alien Invasion")#设置游戏名称
    #开始游戏的主循环
    '''检测到事件类型为quit时，退出游戏'''
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        #让绘制的屏幕可见
        pygame.display.flip()

run_game()