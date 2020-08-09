#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Game.TongLao import TongLao
from Game.XuZhu import XuZhu

xz=XuZhu("李秋水",2000,500)
xz.read()
xz.see_people()
xz.fight_zms()

tl=TongLao("丁春秋",2000,2000)
tl.see_people()
tl.fight_zms()