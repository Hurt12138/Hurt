#!/usr/bin/env python
# -*- coding: utf-8 -*-



class Movie:

    type= ["爱情片" , "动作片", "科幻片"]
    time= {f"120min"}
    pingfen=0
    def __init__(self,pingfen,name,type):
        self.pingfen = pingfen
        self.name = name
        self.type = type

    def yingping(self):
        if self.pingfen >= 8:
            print(f"影评:好看")
        elif self.pingfen <= 4:
            print(f"影评:难看")
        else:
            print(f"影评:一般")


print(Movie.type)
M=Movie(8,"绣春刀","动作片")
print(f"电影:{M.name} 评分: {M.pingfen} 类型: {M.type}")
M.yingping()

