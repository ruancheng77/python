#coding=utf-8
import time
import pygame  # 导入py制作游戏的包
from pygame.locals import *
from sys import exit  # 导入系统相关包

# 敌机类
class Enemy(object):

    def __init__(self,screen):
        # 设置敌机图片
        enemyImageName = "./img/diji.gif"
        self.image = pygame.image.load(enemyImageName).convert()

        # 设置敌机速度
        self.speed = 1

        # 设置敌机坐标
        self.x = 20
        self.y = 200
        # 设置敌机的尺寸
        self.width = 120
        self.height = 84

        # 设置screen
        self.screen = screen

        # 设置敌机子弹集合
        self.bulletList = []

        # 设置敌机运动方向
        self.moveUp = True
        
        # 设置敌机子弹发射间隔
        self.frequency = 100
        self.counter = 0  # 计数器

        # 设置敌机生命
        self.live = 1

        # 设置名称
        self.name = "enemy"
        
        print("敌机启动")

    def draw(self,plane):
        if self.live > 0:
            # 判断玩家飞机是否被敌机的子弹打中,打中->生命减1
            if plane.live > 0:
                for bullet in self.bulletList:
                    if (bullet.x >= plane.x
                        and (bullet.x + bullet.width) <= (plane.x + plane.width)
                        and bullet.y >= plane.y
                        and (bullet.y + bullet.height) <= (plane.y + plane.height - 20)
                        ):
                        plane.live -= 1
                        self.bulletList.remove(bullet)  # 打中飞机的子弹消失
                        print("子弹坐标（%d，%d）,飞机坐标（%d，%d）"%(bullet.x,bullet.y,plane.x,plane.y))
                        print("玩家生命减少1 -----剩余生命条数：%d"%plane.live)
                                
            # 使敌机延时发射子弹
            if  self.counter > self.frequency:
                bullet = Bullet(self)
                self.bulletList.append(bullet)
                self.counter = 0
            else:
                self.counter += 1
            
            # 设置敌机前移
            #self.x += self.speed
            # 敌机向上移动
            if self.moveUp:
                if self.y >= 0:             # 到达上边界之前，上移
                    self.y -= self.speed
                else:                       # 到达上边界时，上移改为下移
                    self.y += self.speed
                    self.moveUp = not self.moveUp
            # 敌机向下移动
            else:
                if self.y <= 400:           # 到达下边界之前，下移
                    self.y += self.speed
                else:                       # 到达下边界时，下移改为上移
                    self.y -= self.speed
                    self.moveUp = not self.moveUp
            # 画出敌机
            self.screen.blit(self.image,(self.x,self.y))
            # 画出敌机的子弹
            for bullet in self.bulletList:
                bullet.draw(self)
        else:
            del self

# 子弹类
class Bullet(object):

    def __init__(self,plane):
        # 线程初始化
        #threading.Thread.__init__(self)
        # 设置子弹的图片
        bulletImageName = "./img/zidan.gif"
        self.image = pygame.image.load(bulletImageName).convert()

        # 设置子弹对象
        if plane.name == "player":
            self.isPlane = True
            # 设置玩家子弹的速度
            self.speed = 1
        elif plane.name == "enemy":
            self.isPlane = False
            # 设置敌机子弹的速度
            self.speed = 2

        # 设置子弹的坐标
        if self.isPlane:
            self.x = plane.x
            self.y = plane.y + 50
        else:
            self.x = plane.x + 100
            self.y = plane.y + 40
        
        # 设置子弹尺寸
        self.width = 13
        self.height = 13
        
        # 设置screen
        self.screen = plane.screen

        # 设置子弹的发射距离
        self.distance = 200

    def draw(self,plane):
        if self.distance >= self.speed:
            if self.isPlane:
                self.x -= self.speed
                self.distance = self.x - 10
            else:
                self.x = self.x + self.speed
                self.distance = 700 - self.x
        else:                                       # 控制子弹消失
            del plane.bulletList[0]
        self.screen.blit(self.image,(self.x,self.y))
        #if self.distance >= self.speed:
         #   self.distance -= self.speed

# 玩家飞机类
class PlayerPlane(object):

    # 初始化方法，完成飞机的默认设置
    def __init__(self,screen):

        # 存储子弹列表
        self.bulletList = []
        
        # 飞机的图片
        planeImageName = "./img/feiji.gif"
        self.image = pygame.image.load(planeImageName).convert()
        
        # 定义飞机的尺寸
        self.width = 120
        self.height = 116
        
        # 设置默认的坐标（左上角坐标为（0,0））
        self.x = 600
        self.y = 200

        # 设置速度
        self.speed = 10

        # 设置screen
        self.screen = screen

        # 设置飞机名字
        self.name = "player"

        # 设置飞机生命数
        self.live = 1

        print("玩家 %s 准备就绪"%self.name)

    # 画飞机方法
    def draw(self,enemy):
        if self.live > 0:
            # 绘画子弹
            for bullet in self.bulletList:
                bullet.draw(self)
            # 判断敌机是否被击中
            if enemy.live > 0:
                for bullet in self.bulletList:
                    if (bullet.x <= (enemy.x + enemy.width)
                        and bullet.x >= enemy.x
                        and bullet.y >= enemy.y
                        and bullet.y <= (enemy.y + enemy.height)
                        ):
                        enemy.live -= 1
                        self.bulletList.remove(bullet)
                        print("Enemy is live -1")
            self.screen.blit(self.image,(self.x,self.y))
        else:
            del self
    # 监听键盘事件，控制飞机移动
    def keyHandle(self, keyValue):
        # 飞机上移
        if keyValue == K_UP:
            # 未超出上边界，可以上移
            if self.y > -10:
                self.y -= self.speed
        # 飞机下移
        elif keyValue == K_DOWN:
            # 未超出下边界，可以下移
            if self.y < 380:
                self.y += self.speed
        # 飞机发射子弹
        elif keyValue == K_SPACE:
            bullet = Bullet(self)            
            self.bulletList.append(bullet)

def main():
    # 初始化pygame
    pygame.init()
    # 设置窗口大小（宽，高）
    SCREEN_SIZE = (720,480)
    # 设置窗口显示模式（尺寸，x,y）：x，y为距离屏幕左上角的坐标
    screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
    # 当第二个参数设置为“FULLSCREEN”时，全屏显示
    #pygame.display.set_mode(SCREEN_SIZE,FULLSCREEN)

    # 设置字体
    #font = pygame.font.SysFont("宋体",16)

    # 加载图片
    backgroud_image_filename = "./img/bg.png"
    background = pygame.image.load(backgroud_image_filename).convert()
    
    # 判断全屏显示标识
    FullScreen = False

    # 创建飞机对象
    player = PlayerPlane(screen)

    # 创建敌机对象
    enemy = Enemy(screen)
    
    while True:
        # 显示背景（背景图片，坐标）
        screen.blit(background,(0,0))
        # 获取事件
        for event in pygame.event.get():
            # 判断事件类型：退出
            if event.type == QUIT:
                exit()
            # 判断事件类型：按下键盘时
            elif event.type == KEYDOWN:
                # 当按下键为f的按键时
                if event.key == K_f:
                    FullScreen = not FullScreen
                    if FullScreen:
                        # 全屏显示
                        screen = pygame.display.set_mode(SCREEN_SIZE,FULLSCREEN)
                    else:
                        # 正常窗口显示
                        screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
                else:
                    player.keyHandle(event.key)

        player.draw(enemy)

        enemy.draw(player)
        
        # 更新窗口
        pygame.display.update()
        # 缓解CPU压力(百分之一秒)
        time.sleep(0.01)

# 定义程序入口
if __name__ == '__main__':
    main()




