import sys
import pygame

'''重构代码结构，存储游戏的运行函数'''

def check_events():
    '''响应鼠标和键盘事件'''
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()


