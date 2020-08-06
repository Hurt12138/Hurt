# -*- coding: utf-8 -*-
import random


def fight():
    #定义血量
    Hp1=1000
    Hp2=1000
    #定义回合数
    num=0
    while True:
        num+=1
        print("第" + str(num) + "轮战斗")
        #定义攻击力范围
        Power1 = random.randint(180,200)
        print("我的攻击力" + str(Power1))
        Power2 = random.randint(100, 250)
        print("对方的攻击力" + str(Power2))
        #每轮双方剩余血量
        my_hp = Hp1-Power2
        your_hp = Hp2-Power1
        #血量降到0以下结束战斗,判定输赢
        if my_hp <= 0 :
            print("输了")
            break
        elif your_hp <= 0 :
            print("赢了")
            break
        else :
            #将每轮剩余血量赋值给各自血量,继续循环
            Hp1 =my_hp
            print("我的血量"+ str(Hp1))
            Hp2 =your_hp
            print("对方血量"+ str(Hp2))


fight()

