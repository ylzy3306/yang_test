#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/8/10 17:45
# @Author : liaochao
# @File   : copy1.py
import random,sys,pygame
from pygame.locals import *
# 蛇身
def main():
    snakeBody = [[300, 300], [280, 300], [260, 300]]
    # 目标方块的初始位置
    targetPosition = [100, 100]
    # 蛇的初始位置
    snakePosition = [300, 300]
    # 目标颜色
    redColor = pygame.Color(255, 0, 0)
    # 游戏背景色
    blackColor = pygame.Color(0, 0, 0)
    # 蛇的背景色
    whiteColor = pygame.Color(255, 255, 255)
    # 游戏运行的速度
    fpsclock = pygame.time.Clock()
    targeFlag = 1
    playsurface = pygame.display.set_mode()