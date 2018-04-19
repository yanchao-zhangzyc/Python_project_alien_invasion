import pygame
class Ship():
    def __init__(self,screen):
        '''初始化飞船并设置其初始位置'''
        self.screen=screen
        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('image/rocket.png')
        self.rect=self.image.get_rect()#显示图片
        self.screen_rect=screen.get_rect()
        #设置图片的坐标,设置在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.bottom
    def blitme(self):
        #在制定位置绘制飞船
        self.screen.blit(self.image,self.rect)
