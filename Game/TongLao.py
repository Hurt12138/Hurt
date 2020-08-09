#!/usr/bin/env python
# -*- coding: utf-8 -*-

#定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
#see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
# 如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
#fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
# 需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

class TongLao:
    HP_TL=2000
    Power_TL=300
    def __init__(self,name,HP_DR,Power_DR):
        self.name = name
        self.HP_DR = HP_DR
        self.Power_DR =Power_DR
    def see_people(self):
        print("叫阵:")
        if self.name == "WYZ":
            print("师弟！！！！")
        elif self.name == "李秋水":
            print("呸，贱人")
        elif self.name == "丁春秋":
            print("叛徒！我杀了你")
    def fight_zms(self):
        print("战斗开始")
        self.HP_TL = self.HP_TL/2
        self.Power_TL = self.Power_TL*10
        if self.HP_TL-self.Power_DR > self.HP_DR-self.Power_TL:
            print("童姥赢了")
        elif self.HP_TL-self.Power_DR == self.HP_DR-self.Power_TL:
            print("平手,承让")
        else:
            print("童姥输了")




