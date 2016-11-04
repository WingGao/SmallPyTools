# coding=utf-8
import os
from PIL import Image

dir = '/Users/wing/Documents/Temp/icon'
des_dir = '/Users/wing/Documents/Temp/icon2'


def reszie():
    w = 55
    h = 55
    for i in os.listdir(dir):
        img = Image.open(os.path.join(dir, i))
        img.thumbnail((w, h), Image.ANTIALIAS)
        # whr = float(w) / h
        # iwhr = float(img.size[0]) / img.size[1]
        # iw = w
        # ih = h
        # if iwhr > whr:
        #     # 太宽，以长为标准
        #     iw = int(iwhr * ih)
        # else:
        #     ih = int(iw / iwhr)
        # img = img.resize((iw, ih))
        # left = int((iw - w) / 2)
        # upper = int((iwhr / ih) / 2)
        # box = (left, upper, w + left, h + upper)
        # img = img.crop(box)
        img.save(os.path.join(des_dir, i), quality=100)
        print i


def rename():
    if not os.path.exists(des_dir):
        os.mkdir(des_dir)
    for i in os.listdir(dir):
        r = i
        print i
        os.rename(os.path.join(dir, i), os.path.join(des_dir, i))


reszie()
