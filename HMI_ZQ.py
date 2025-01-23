#!usr/bin/env python
# _*_ coding: utf-8 _*_

import sys
import subprocess
import uiautomator2 as u2
import keyboard
import psutil

d = u2.connect('198.18.1.18:7777')
d1 = u2.connect('191QJEZPNEWVT')
sys.path.append(r'D:\ToolServerX86_64\tae_engine\customlib\ImageTools')
from Img_PaddleOCR_cmd import run as ocr
from Image_Tools import HMI
import time
from adbTool import ADB
import cv2
from IC import *
from appium.webdriver.common.touch_action import TouchAction

class Adb(object):

    def __init__(self):
        self.ADB = ADB()
        self.HMI = HMI()
        self.ocr = ocr()
        self.isConnected = False
        self.qnx = QNX()

    def connect(self):
        self.isConnected = True

    def disconnect(self):
        self.isConnected = False

    def Icon_Coord(self, Icon_ROI):
        with open(Icon_ROI, "r") as txt_file:
            self.iconROI = []  # icon 坐标 Left Upper Width Height
            for line in txt_file.readlines():
                line = line.split(':')
                self.iconROI.append(int(line[1]))

        x_coord = round(self.iconROI[2] / 2) + self.iconROI[0]
        y_coord = round(self.iconROI[3] / 2) + self.iconROI[1]
        coord = [x_coord, y_coord]
        print(coord)
        return coord

    def Click(self, Icon_ROI):
        Icon_roi = r'D:\\FY_HMI\\workspace\\Image\\ROI\\Meter\\' + Icon_ROI
        Icon_ROI = Icon_roi
        x_coord = self.Icon_Coord(Icon_ROI)[0]
        y_coord = self.Icon_Coord(Icon_ROI)[1]
        Result = self.ADB.Click(x_coord, y_coord)
        print('ddddddddddd',Result)
        return [Result]
    #新增
    def Click_Phone(self, Icon_ROI):
        Icon_roi = r'D:\\FY_HMI\\workspace\\Image\\ROI\\Meter\\' + Icon_ROI
        Icon_ROI = Icon_roi
        x_coord = self.Icon_Coord(Icon_ROI)[0]
        y_coord = self.Icon_Coord(Icon_ROI)[1]
        Result = self.ADB.Click_Phone(x_coord, y_coord)
        print('ddddddddddd',Result)
        return [Result]

    def Click_text(self, Icon_ROI):
        Aoteman = d(text=Icon_ROI).bounds()
        # 左上坐标x y
        X1 = Aoteman[0]
        Y1 = Aoteman[1]
        # 右下坐标 x y
        X2 = Aoteman[2]
        Y2 = Aoteman[3]
        X = (X1 + X2) / 2
        Y = (Y1 + Y2) / 2
        print(X, Y)
        Result = self.ADB.Click(X, Y)
        return [Result]

    def Click_resourceId(self, Icon_ROI):
        Aoteman = d(resourceId=Icon_ROI).bounds()
        # 左上坐标x y
        X1 = Aoteman[0]
        Y1 = Aoteman[1]
        # 右下坐标 x y
        X2 = Aoteman[2]
        Y2 = Aoteman[3]
        X = (X1 + X2) / 2
        Y = (Y1 + Y2) / 2
        print(X, Y)
        Result = self.ADB.Click(X, Y)
        return [Result]

    def Click_description(self, Icon_ROI):
        Aoteman = d(description=Icon_ROI).bounds()
        # 左上坐标x y
        X1 = Aoteman[0]
        Y1 = Aoteman[1]
        # 右下坐标 x y
        X2 = Aoteman[2]
        Y2 = Aoteman[3]
        X = (X1 + X2) / 2
        Y = (Y1 + Y2) / 2
        print(X, Y)
        Result = self.ADB.Click(X, Y)
        return [Result]

    def Double_Click(self, Icon_ROI):
        Icon_roi = r'D:\\FY_HMI\\workspace\\Image\\ROI\\Meter\\' + Icon_ROI
        Icon_ROI = Icon_roi
        x_coord = self.Icon_Coord(Icon_ROI)[0]
        y_coord = self.Icon_Coord(Icon_ROI)[1]
        Result = self.ADB.Double_click(x_coord, y_coord)
        return [Result]

    def Swipe(self, Icon_ROI_1, Icon_ROI_2):
        Icon_roi1 = r'D:\\FY_HMI\\workspace\\Image\\ROI\\Meter\\' + Icon_ROI_1
        Icon_ROI_1 = Icon_roi1
        Icon_roi2 = r'D:\\FY_HMI\\workspace\\Image\\ROI\\Meter\\' + Icon_ROI_2
        Icon_ROI_2 = Icon_roi2
        x_coord_1 = self.Icon_Coord(Icon_ROI_1)[0]
        y_coord_1 = self.Icon_Coord(Icon_ROI_1)[1]
        x_coord_2 = self.Icon_Coord(Icon_ROI_2)[0]
        y_coord_2 = self.Icon_Coord(Icon_ROI_2)[1]
        Result = self.ADB.Swipe(x_coord_1, y_coord_1, x_coord_2, y_coord_2)
        return [Result]

    def Swipe_treble(self, Icon_ROI_1, Icon_ROI_2, Icon_ROI_3):
        Icon_roi1 = r'D:\\FY_HMI\\workspace\\Image\\ROI\\Meter\\' + Icon_ROI_1
        Icon_ROI_1 = Icon_roi1
        Icon_roi2 = r'D:\\FY_HMI\\workspace\\Image\\ROI\\Meter\\' + Icon_ROI_2
        Icon_ROI_2 = Icon_roi2
        Icon_roi3 = r'D:\\FY_HMI\\workspace\\Image\\ROI\\Meter\\' + Icon_ROI_3
        Icon_ROI_3 = Icon_roi3
        x_coord_1 = self.Icon_Coord(Icon_ROI_1)[0]
        y_coord_1 = self.Icon_Coord(Icon_ROI_1)[1]
        x_coord_2 = self.Icon_Coord(Icon_ROI_2)[0]
        y_coord_2 = self.Icon_Coord(Icon_ROI_2)[1]
        x_coord_3 = self.Icon_Coord(Icon_ROI_3)[0]
        y_coord_3 = self.Icon_Coord(Icon_ROI_3)[1]
        points = [(x_coord_1,y_coord_1),(x_coord_2,y_coord_2),(x_coord_3,y_coord_3)]
        Result = d.swipe_points(points,0.2)
        return [Result]

    def Swipe_text(self, Icon_ROI_1, Icon_ROI_2):
        Aoteman1 = d(text=Icon_ROI_1).bounds()
        Aoteman2 = d(text=Icon_ROI_2).bounds()
        # 左上坐标x y
        X1_1 = Aoteman1[0]
        Y1_1 = Aoteman1[1]
        # 右下坐标 x y
        X1_2 = Aoteman1[2]
        Y1_2 = Aoteman1[3]
        X1 = (X1_1 + X1_2) / 2
        Y1 = (Y1_1 + Y1_2) / 2

        X2_1 = Aoteman2[0]
        Y2_1 = Aoteman2[1]
        # 右下坐标 x y
        X2_2 = Aoteman2[2]
        Y2_2 = Aoteman2[3]
        X2 = (X2_1 + X2_2) / 2
        Y2 = (Y2_1 + Y2_2) / 2
        print(X1, Y1 , X2 ,Y2 )
        Result = self.ADB.Swipe(X1, Y1, X2, Y2)
        return [Result]

    def Swipe_resourceId(self, Icon_ROI_1, Icon_ROI_2):
        Aoteman1 = d(resourceId=Icon_ROI_1).bounds()
        Aoteman2 = d(resourceId=Icon_ROI_2).bounds()
        # 左上坐标x y
        X1_1 = Aoteman1[0]
        Y1_1 = Aoteman1[1]
        # 右下坐标 x y
        X1_2 = Aoteman1[2]
        Y1_2 = Aoteman1[3]
        X1 = (X1_1 + X1_2) / 2
        Y1 = (Y1_1 + Y1_2) / 2

        X2_1 = Aoteman2[0]
        Y2_1 = Aoteman2[1]
        # 右下坐标 x y
        X2_2 = Aoteman2[2]
        Y2_2 = Aoteman2[3]
        X2 = (X2_1 + X2_2) / 2
        Y2 = (Y2_1 + Y2_2) / 2
        print(X1, Y1 , X2 ,Y2 )
        Result = self.ADB.Swipe(X1, Y1, X2, Y2)
        return [Result]

    def Swipe_description(self, Icon_ROI_1, Icon_ROI_2):
        Aoteman1 = d(description=Icon_ROI_1).bounds()
        Aoteman2 = d(description=Icon_ROI_2).bounds()
        # 左上坐标x y
        X1_1 = Aoteman1[0]
        Y1_1 = Aoteman1[1]
        # 右下坐标 x y
        X1_2 = Aoteman1[2]
        Y1_2 = Aoteman1[3]
        X1 = (X1_1 + X1_2) / 2
        Y1 = (Y1_1 + Y1_2) / 2

        X2_1 = Aoteman2[0]
        Y2_1 = Aoteman2[1]
        # 右下坐标 x y
        X2_2 = Aoteman2[2]
        Y2_2 = Aoteman2[3]
        X2 = (X2_1 + X2_2) / 2
        Y2 = (Y2_1 + Y2_2) / 2
        print(X1, Y1 , X2 ,Y2 )
        Result = self.ADB.Swipe(X1, Y1, X2, Y2)
        return [Result]
    #新增
    def Swipe_Phone(self, Icon_ROI_1, Icon_ROI_2):
        Icon_roi1 = r'D:\\FY_HMI\\workspace\\Image\\ROI\\Meter\\' + Icon_ROI_1
        Icon_ROI_1 = Icon_roi1
        Icon_roi2 = r'D:\\FY_HMI\\workspace\\Image\\ROI\\Meter\\' + Icon_ROI_2
        Icon_ROI_2 = Icon_roi2
        x_coord_1 = self.Icon_Coord(Icon_ROI_1)[0]
        y_coord_1 = self.Icon_Coord(Icon_ROI_1)[1]
        x_coord_2 = self.Icon_Coord(Icon_ROI_2)[0]
        y_coord_2 = self.Icon_Coord(Icon_ROI_2)[1]
        Result = self.ADB.Swipe_Phone(x_coord_1, y_coord_1, x_coord_2, y_coord_2)
        return [Result]

    def Swipe_Phone_treble(self, Icon_ROI_1, Icon_ROI_2, Icon_ROI_3):
        Icon_roi1 = r'D:\\FY_HMI\\workspace\\Image\\ROI\\Meter\\' + Icon_ROI_1
        Icon_ROI_1 = Icon_roi1
        Icon_roi2 = r'D:\\FY_HMI\\workspace\\Image\\ROI\\Meter\\' + Icon_ROI_2
        Icon_ROI_2 = Icon_roi2
        Icon_roi3 = r'D:\\FY_HMI\\workspace\\Image\\ROI\\Meter\\' + Icon_ROI_3
        Icon_ROI_3 = Icon_roi3
        x_coord_1 = self.Icon_Coord(Icon_ROI_1)[0]
        y_coord_1 = self.Icon_Coord(Icon_ROI_1)[1]
        x_coord_2 = self.Icon_Coord(Icon_ROI_2)[0]
        y_coord_2 = self.Icon_Coord(Icon_ROI_2)[1]
        x_coord_3 = self.Icon_Coord(Icon_ROI_3)[0]
        y_coord_3 = self.Icon_Coord(Icon_ROI_3)[1]
        points = [(x_coord_1,y_coord_1),(x_coord_2,y_coord_2),(x_coord_3,y_coord_3)]
        Result = d1.swipe_points(points,0.2)
        return [Result]

    def Press_Hold(self, Icon_ROI, Hold_time):
        Icon_roi = r'D:\\FY_HMI\\workspace\\Image\\ROI\\Meter\\' + Icon_ROI
        Icon_ROI = Icon_roi
        x_coord = self.Icon_Coord(Icon_ROI)[0]
        y_coord = self.Icon_Coord(Icon_ROI)[1]
        Result = self.ADB.Press_Hold(x_coord, y_coord, Hold_time)
        return [Result]

    def Press_Hold_text(self, Icon_ROI, Hold_time):
        Aoteman = d(text=Icon_ROI).bounds()
        # 左上坐标x y
        X1 = Aoteman[0]
        Y1 = Aoteman[1]
        # 右下坐标 x y
        X2 = Aoteman[2]
        Y2 = Aoteman[3]
        X = (X1 + X2) / 2
        Y = (Y1 + Y2) / 2
        print(X, Y)
        Result = self.ADB.Press_Hold(X, Y, Hold_time)
        return [Result]

    def Press_Hold_resourceId(self, Icon_ROI, Hold_time):
        Aoteman = d(resourceId=Icon_ROI).bounds()
        # 左上坐标x y
        X1 = Aoteman[0]
        Y1 = Aoteman[1]
        # 右下坐标 x y
        X2 = Aoteman[2]
        Y2 = Aoteman[3]
        X = (X1 + X2) / 2
        Y = (Y1 + Y2) / 2
        print(X, Y)
        Result = self.ADB.Press_Hold(X, Y, Hold_time)
        return [Result]

    def Press_Hold_description(self, Icon_ROI, Hold_time):
        Aoteman = d(description=Icon_ROI).bounds()
        # 左上坐标x y
        X1 = Aoteman[0]
        Y1 = Aoteman[1]
        # 右下坐标 x y
        X2 = Aoteman[2]
        Y2 = Aoteman[3]
        X = (X1 + X2) / 2
        Y = (Y1 + Y2) / 2
        print(X, Y)
        Result = self.ADB.Press_Hold(X, Y, Hold_time)
        return [Result]


    def IC_Screenshot(self, PCImage):
        date = time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())
        Image = 'D:\\FY_HMI\\workspace\\Image\\Screen\\IC_Screen\\' + PCImage
        Result = self.ADB.IC_screencap(DUT=date, PCImage=Image)
        return [Result, Image]

    def ICS_Screenshot(self, PCImage):
        date = time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())
        Image = 'D:\\FY_HMI\\workspace\\Image\\Screen\\ICS_Screen\\' + PCImage
        Result = self.ADB.ICS_screencap(DUT=date, PCImage=Image)
        return [Result, Image]

    def Phone_Screenshot(self, PCImage):
        date = time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())
        Image = 'D:\\FY_HMI\\workspace\\Image\\Screen\\Phone_Screen\\' + PCImage
        Result = self.ADB.Phone_screencap(DUT=date, PCImage=Image)
        return [Result, Image]

    def Devices(self):
        Result = self.ADB.Devices()
        print(Result)
        return Result

    def Home(self):
        Result = self.ADB.Home()
        return Result

    def Home_Phone(self):
        Result = self.ADB.Home_Phone()
        return Result

    def Back(self):
        Result = self.ADB.Back()
        return Result

    def Back_Phone(self):
        Result = self.ADB.Back_Phone()
        return Result

    def IC_ADB_Paddle_OCR(self, PCImage, ROI):
        roi = 'D:\\FY_HMI\\workspace\\Image\\ROI\\OCR\\' + ROI
        ROI = roi
        img = self.IC_Screenshot(PCImage)
        img = str(img[1])
        Result = self.ocr.run_cmd(img, ROI)
        print(Result)
        return [Result]

    def ICS_ADB_Paddle_OCR(self, PCImage, ROI):
        roi = 'D:\\FY_HMI\\workspace\\Image\\ROI\\OCR\\' + ROI
        ROI = roi
        img = self.ICS_Screenshot(PCImage)
        img = str(img[1])
        print(img, ROI)
        Result = self.ocr.run_cmd(img, ROI)
        # print(Result)
        return [Result]

    def ICS_ADB_Paddle_OCR_text(self, Icon_ROI):
        Aoteman = d(text=Icon_ROI).bounds()
        # print(Aoteman)
        # 左上坐标x y
        X1 = Aoteman[0]
        Y1 = Aoteman[1]
        # 右下坐标 x y
        X2 = Aoteman[2]
        Y2 = Aoteman[3]
        W = X2 - X1
        H = Y2 - Y1
        # time.sleep(2)
        # with open('D:\FY_HMI\workspace\Image\ROI\OCR\IC_0519.txt','w')as f:
        #     f.write(str(a))
        my_list1 = ["X:"]
        my_list2 = ["Y:"]
        my_list3 = ["W:"]
        my_list4 = ["H:"]
        with open('D:\\FY_HMI\\workspace\\Image\\ROI\\OCR\\IC_0521.txt', 'w') as f:
            for item in my_list1:
                f.write(item + ' ' + str(X1) + '\n')
            for item in my_list2:
                f.write(item + ' ' + str(Y1) + '\n')
            for item in my_list3:
                f.write(item + ' ' + str(W) + '\n')
            for item in my_list4:
                f.write(item + ' ' + str(H))
        PCImage = '7.png'
        img = self.ICS_Screenshot(PCImage)
        img = str(img[1])
        time.sleep(1)
        ROI = 'D:\\FY_HMI\\workspace\\Image\\ROI\\OCR\\IC_0521.txt'
        # print(img, ROI)
        Result = self.ocr.run_cmd(img, ROI)
        print(Result)
        return [Result]

    def ICS_ADB_Paddle_OCR_resourceId(self, Icon_ROI):
        Aoteman = d(resourceId=Icon_ROI).bounds()
        # 左上坐标x y
        X1 = Aoteman[0]
        Y1 = Aoteman[1]
        # 右下坐标 x y
        X2 = Aoteman[2]
        Y2 = Aoteman[3]
        W = X2 - X1
        H = Y2 - Y1
        # with open('D:\FY_HMI\workspace\Image\ROI\OCR\IC_0519.txt','w')as f:
        #     f.write(str(a))
        my_list1 = ["X:"]
        my_list2 = ["Y:"]
        my_list3 = ["W:"]
        my_list4 = ["H:"]
        with open('D:\FY_HMI\workspace\Image\ROI\OCR\IC_0521.txt', 'w') as f:
            for item in my_list1:
                f.write(item + ' ' + str(X1) + '\n')
            for item in my_list2:
                f.write(item + ' ' + str(Y1) + '\n')
            for item in my_list3:
                f.write(item + ' ' + str(W) + '\n')
            for item in my_list4:
                f.write(item + ' ' + str(H))
        img = self.ICS_Screenshot(PCImage)
        img = str(img[1])
        time.sleep(1)
        ROI = 'D:\\FY_HMI\\workspace\\Image\\ROI\\OCR\\IC_0521.txt'
        # print(img, ROI)
        Result = self.ocr.run_cmd(img, ROI)
        print(Result)
        return [Result]

    def ICS_ADB_Paddle_OCR_description(self, Icon_ROI):
        Aoteman = d(description=Icon_ROI).bounds()
        # 左上坐标x y
        X1 = Aoteman[0]
        Y1 = Aoteman[1]
        # 右下坐标 x y
        X2 = Aoteman[2]
        Y2 = Aoteman[3]
        W = X2 - X1
        H = Y2 - Y1
        # with open('D:\FY_HMI\workspace\Image\ROI\OCR\IC_0519.txt','w')as f:
        #     f.write(str(a))
        my_list1 = ["X:"]
        my_list2 = ["Y:"]
        my_list3 = ["W:"]
        my_list4 = ["H:"]
        with open('D:\FY_HMI\workspace\Image\ROI\OCR\IC_0521.txt', 'w') as f:
            for item in my_list1:
                f.write(item + ' ' + str(X1) + '\n')
            for item in my_list2:
                f.write(item + ' ' + str(Y1) + '\n')
            for item in my_list3:
                f.write(item + ' ' + str(W) + '\n')
            for item in my_list4:
                f.write(item + ' ' + str(H))
        img = self.ICS_Screenshot(PCImage)
        img = str(img[1])
        time.sleep(1)
        # print(img, ROI)
        ROI = 'D:\\FY_HMI\\workspace\\Image\\ROI\\OCR\\IC_0521.txt'
        Result = self.ocr.run_cmd(img, ROI)
        print(Result)
        return [Result]

    def Phone_ADB_Paddle_OCR(self, PCImage, ROI):
        roi = 'D:\\FY_HMI\\workspace\\Image\\ROI\\OCR\\' + ROI
        ROI = roi
        img = self.Phone_Screenshot(PCImage)
        img = str(img[1])
        print(img, ROI)
        Result = self.ocr.run_cmd(img, ROI)
        # print(Result)
        return [Result]

    def IC_ADB_Image_Match_Temp(self, PCImage, img_target):
        # roi = 'D:\\FY_HMI\\workspace\\Image\\ROI\\ICON\\' + ROI
        # ROI = roi
        IMG_target = 'D:\\FY_HMI\\workspace\\Image\\ROI\\ICON\\' + img_target
        img_target = IMG_target
        img_ori = self.IC_Screenshot(PCImage)
        img_ori = str(img_ori[1])
        Result = self.HMI.IC_img_tpl_match(img_ori, img_target)
        print(Result)
        print(int(Result[0]))
        if Result[0] > 800:
            print('该模板匹配成功\n匹配分数 =', Result[0])
            result = 'Pass'
        else:
            print('该模板匹配失败\n匹配分数 =', Result[0])
            result = 'Not Pass'
        # return [Result[0]]
        return [int(Result[0])]

    # def ICS_ADB_Image_Match_Temp(self, PCImage, img_target):
    #         IMG_target = 'D:\\FY_HMI\\workspace\\Image\\ROI\\ICON\\' + img_target
    #         img_target = IMG_target
    #         img_ori = self.ICS_Screenshot(PCImage)
    #         img_ori = str(img_ori[1])
    #         Result = self.HMI.ICS_img_tpl_match(img_ori, img_target, ROI=None)
    #         print(Result)
    #         if Result[0] > 800:
    #             print('该模板匹配成功\n匹配分数 =', Result[0])
    #             result = 'Pass'
    #         else:
    #             print('该模板匹配失败\n匹配分数 =', Result[0])
    #             result = 'Not Pass'
    #         # print('kkkkkkkkkkkkkkkkkkkkk',result,Result[0])
    #         return [Result[0]]
    def ICS_ADB_Image_Match_Temp(self, PCImage, img_target):
        # roi = 'D:\\FY_HMI\\workspace\\Image\\ROI\\ICON\\' + ROI
        # ROI = roi
        IMG_target = 'D:\\FY_HMI\\workspace\\Image\\ROI\\ICON\\' + img_target
        img_target = IMG_target
        img_ori = self.ICS_Screenshot(PCImage)
        img_ori = str(img_ori[1])
        Result = self.HMI.ICS_img_tpl_match(img_ori, img_target)
        print(Result)
        print(int(Result[0]))
        if Result[0] > 800:
            print('该模板匹配成功\n匹配分数 =', Result[0])
            result = 'Pass'
        else:
            print('该模板匹配失败\n匹配分数 =', Result[0])
            result = 'Not Pass'
        # print('kkkkkkkkkkkkkkkkkkkkk',result,Result[0])
        return [int(Result[0])]
        # if ROI:
        #     roi = 'D:\\FY_HMI\\workspace\\Image\\ROI\\ICON\\' + ROI
        #     ROI = roi
        #     IMG_target = 'D:\\FY_HMI\\workspace\\Image\\ROI\\ICON\\' + img_target
        #     img_target = IMG_target
        #     img_ori = self.ICS_Screenshot(PCImage)
        #     img_ori = str(img_ori[1])
        #     Result = self.HMI.ICS_img_tpl_match(img_ori, img_target, ROI)
        #     print(Result)
        #     if Result[0] > 800:
        #         print('该模板匹配成功\n匹配分数 =', Result[0])
        #         result = 'Pass'
        #     else:
        #         print('该模板匹配失败\n匹配分数 =', Result[0])
        #         result = 'Not Pass'
        #     # print('kkkkkkkkkkkkkkkkkkkkk',result,Result[0])
        #     return [Result[0]]

    def Phone_ADB_Image_Match_Temp(self, PCImage, img_target):
        # roi = 'D:\\FY_HMI\\workspace\\Image\\ROI\\ICON\\' + ROI
        # ROI = roi
        IMG_target = 'D:\\FY_HMI\\workspace\\Image\\ROI\\ICON\\' + img_target
        img_target = IMG_target
        img_ori = self.Phone_Screenshot(PCImage)
        img_ori = str(img_ori[1])
        Result = self.HMI.IC_img_tpl_match(img_ori, img_target)
        print(Result)
        print(int(Result[0]))
        if Result[0] > 800:
            print('该模板匹配成功\n匹配分数 =', Result[0])
            result = 'Pass'
        else:
            print('该模板匹配失败\n匹配分数 =', Result[0])
            result = 'Not Pass'
        # return [Result[0]]
        return [int(Result[0])]

    def IC_ADB_Color_Rec(self, PCImage, ROI):
        roi = 'D:/FY_HMI/workspace/Image/ROI/Color/' + ROI
        ROI = roi
        img_ori = self.IC_Screenshot(PCImage)
        img_ori = str(img_ori[1])
        time.sleep(2)
        print(img_ori, ROI)
        Result1 = self.HMI.color_rec(img_ori, ROI)
        Result = Result1[1]
        print(Result)
        return [Result]

    def ICS_ADB_Color_Rec_text(self, Icon_ROI):
        Aoteman = d(text=Icon_ROI).bounds()
        # 左上坐标x y
        X1 = Aoteman[0]
        Y1 = Aoteman[1]
        # 右下坐标 x y
        X2 = Aoteman[2]
        Y2 = Aoteman[3]
        W = X2 - X1
        H = Y2 - Y1
        # with open('D:\FY_HMI\workspace\Image\ROI\OCR\IC_0519.txt','w')as f:
        #     f.write(str(a))
        my_list1 = ["X:"]
        my_list2 = ["Y:"]
        my_list3 = ["W:"]
        my_list4 = ["H:"]
        with open('D:\FY_HMI\workspace\Image\ROI\OCR\IC_0520.txt', 'w') as f:
            for item in my_list1:
                f.write(item + ' ' + str(X1) + '\n')
            for item in my_list2:
                f.write(item + ' ' + str(Y1) + '\n')
            for item in my_list3:
                f.write(item + ' ' + str(W) + '\n')
            for item in my_list4:
                f.write(item + ' ' + str(H))
        PCImage = '7.png'
        img = self.ICS_Screenshot(PCImage)
        img = str(img[1])
        time.sleep(1)
        ROI = 'D:\\FY_HMI\\workspace\\Image\\ROI\\OCR\\IC_0520.txt'
        # print(img, ROI)
        Result1 = self.HMI.color_rec(img, ROI)
        Result = Result1[1]
        print(Result)
        return [Result]

    def ICS_ADB_Color_Rec_resourceId(self, Icon_ROI):
        Aoteman = d(resourceId=Icon_ROI).bounds()
        # 左上坐标x y
        X1 = Aoteman[0]
        Y1 = Aoteman[1]
        # 右下坐标 x y
        X2 = Aoteman[2]
        Y2 = Aoteman[3]
        W = X2 - X1
        H = Y2 - Y1
        # with open('D:\FY_HMI\workspace\Image\ROI\OCR\IC_0519.txt','w')as f:
        #     f.write(str(a))
        my_list1 = ["X:"]
        my_list2 = ["Y:"]
        my_list3 = ["W:"]
        my_list4 = ["H:"]
        with open('D:\FY_HMI\workspace\Image\ROI\OCR\IC_0520.txt', 'w') as f:
            for item in my_list1:
                f.write(item + ' ' + str(X1) + '\n')
            for item in my_list2:
                f.write(item + ' ' + str(Y1) + '\n')
            for item in my_list3:
                f.write(item + ' ' + str(W) + '\n')
            for item in my_list4:
                f.write(item + ' ' + str(H))
        PCImage = '7.png'
        img = self.ICS_Screenshot(PCImage)
        img = str(img[1])
        time.sleep(1)
        ROI = 'D:\\FY_HMI\\workspace\\Image\\ROI\\OCR\\IC_0520.txt'
        # print(img, ROI)
        Result1 = self.HMI.color_rec(img, ROI)
        Result = Result1[1]
        print(Result)
        return [Result]

    def ICS_ADB_Color_Rec_description(self, Icon_ROI):
        Aoteman = d(description=Icon_ROI).bounds()
        # 左上坐标x y
        X1 = Aoteman[0]
        Y1 = Aoteman[1]
        # 右下坐标 x y
        X2 = Aoteman[2]
        Y2 = Aoteman[3]
        W = X2 - X1
        H = Y2 - Y1
        # with open('D:\FY_HMI\workspace\Image\ROI\OCR\IC_0519.txt','w')as f:
        #     f.write(str(a))
        my_list1 = ["X:"]
        my_list2 = ["Y:"]
        my_list3 = ["W:"]
        my_list4 = ["H:"]
        with open('D:\FY_HMI\workspace\Image\ROI\OCR\IC_0520.txt', 'w') as f:
            for item in my_list1:
                f.write(item + ' ' + str(X1) + '\n')
            for item in my_list2:
                f.write(item + ' ' + str(Y1) + '\n')
            for item in my_list3:
                f.write(item + ' ' + str(W) + '\n')
            for item in my_list4:
                f.write(item + ' ' + str(H))
        PCImage = '7.png'
        img = self.ICS_Screenshot(PCImage)
        img = str(img[1])
        time.sleep(1)
        ROI = 'D:\\FY_HMI\\workspace\\Image\\ROI\\OCR\\IC_0520.txt'
        # print(img, ROI)
        Result1 = self.HMI.color_rec(img, ROI)
        Result = Result1[1]
        print(Result)
        return [Result]

    def ICS_ADB_Color_Rec(self, PCImage, ROI):
        roi = 'D:\\FY_HMI\\workspace\\Image\\ROI\\Color\\' + ROI
        ROI = roi
        img_ori = self.ICS_Screenshot(PCImage)
        img_ori = str(img_ori[1])
        Result1 = self.HMI.color_rec(img_ori, ROI)
        Result = Result1[1]
        print(Result)
        return [Result]

    def Phone_ADB_Color_Rec(self, PCImage, ROI):
        roi = 'D:/FY_HMI/workspace/Image/ROI/Color/' + ROI
        ROI = roi
        img_ori = self.IC_Screenshot(PCImage)
        img_ori = str(img_ori[1])
        time.sleep(2)
        print(img_ori, ROI)
        Result1 = self.HMI.color_rec(img_ori, ROI)
        Result = Result1[1]
        print(Result)
        return [Result]

    def qnx_screen(self, path=None):
        image_path = self.qnx.screen(path)
        return [image_path]

    def QNX_Image_Match_Temp(self, PCImage, img_target):
        # roi = 'D:\\FY_HMI\\workspace\\Image\\ROI\\ICON\\' + ROI
        # ROI = roi
        IMG_target = 'D:\\FY_HMI\\workspace\\Image\\ROI\\ICON\\' + img_target
        img_target = IMG_target
        img_ori = self.qnx_screen(PCImage)
        img_ori = str(img_ori[0])
        Result = self.HMI.ICS_img_tpl_match(img_ori, img_target)
        # print(Result)
        print(int(Result[0]))
        if Result[0] > 850:
            print('该模板匹配成功\n匹配分数 =', Result[0])
            result = 'Pass'
        else:
            print('该模板匹配失败\n匹配分数 =', Result[0])
            result = 'Not Pass'
            # print(type(Result))
        return [int(Result[0])]

    def QNX_Color_Rec(self, PCImage, ROI):
        roi = 'D:\\FY_HMI\\workspace\\Image\\ROI\\Color\\' + ROI
        ROI = roi
        img_ori = self.qnx_screen(PCImage)
        img_ori = str(img_ori[0])
        time.sleep(2)
        # print(img_ori, ROI)
        Result1 = self.HMI.color_rec(img_ori, ROI)
        Result = Result1[1]
        print(Result)
        print(type(Result))
        return [Result]

    def QNX_Paddle_OCR(self, PCImage, ROI):
        roi = 'D:\\FY_HMI\\workspace\\Image\\ROI\\OCR\\' + ROI
        ROI = roi
        img = self.qnx_screen(PCImage)
        img = str(img[0])
        # print(img, ROI)
        Result = self.ocr.run_cmd(img, ROI)
        print(Result)
        print(type(Result))
        return [Result]

#获取开关状态
    def Get_info(self, description, info):
        Aoteman = d(description=description).info[info]
        Result = Aoteman
        print(Result)
        return [Result]
#捕获日志
    def Cap_log(self, content):
        timenow = self.ADB.timenow()
        time.sleep(1)
        content_logd = 'logd_' + content + str(timenow)
        content_dropbox = 'dropbox_' + content + str(timenow)
        content_tombstones = 'tombstones_' + content + str(timenow)
        content_anr = 'anr_' + content + str(timenow)
        content_cdclogs = 'cdclogs_' + content + str(timenow)
        content_critical = 'critical_' + content + str(timenow)
        content_slog = 'slog_' + content + str(timenow)
        content_bluetooth = 'bluetooth_' + content + str(timenow)
        self.ADB.logd(content_logd)
        self.ADB.dropbox(content_dropbox)
        self.ADB.tombstones(content_tombstones)
        self.ADB.anr(content_anr)
        self.ADB.cdclogs(content_cdclogs)
        self.ADB.dropbox(content_critical)
        self.ADB.dropbox(content_slog)
        self.ADB.dropbox(content_bluetooth)
        Result = timenow
        return [Result]

#开始录制DLT日志
    def DLT_log_start(self, content='DLTLOG'):
        date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        cmd = 'D:\\Software\\DLTViewer-2.23.0-STABLE-qt5.15.2-r962_msvc2019_x64-win64-OSS-Release\\DLTViewer-2.23.0-STABLE-qt5.15.2-r962_msvc2019_x64-win64-OSS-Release\\dlt-viewer.exe -l D:\\dlt_log\\'+ content + '_' + date_time + '.dlt'
        os.popen(cmd)
        return [date_time]

    def DLT_log_end(self,program_name="dlt-viewer.exe"):
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'] == program_name:
                    proc.terminate()
                    print(f"已关闭程序 {program_name}，进程 ID: {proc.info['pid']}")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

    def Phone_log(self,content):
        # 连接设备
        date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        cmd = 'adb logcat -v time > D:\\FYlog\\!timing!\\'+ content + date_time + '.txt'
        subprocess.popen(cmd)

if __name__ == '__main__':
    Task2 = Adb()
    # Task2.qnx_screen('qnx.png')
    # Task2.QNX_Color_Rec('qnx.png','c.txt')
    # Task2.QNX_Paddle_OCR('qnx.png','okm.txt')
    # Task2.IC_Screenshot('7.png')
    # print(Task2.QNX_Image_Match_Temp('主驾安全带未系.png',r'主驾安全带未系.png',r'主驾安全带未系.txt'))
    # Task2.ICS_Screenshot('7.png')
    # Task2.Devices()
    # Task2.ICS_ADB_Paddle_OCR_text('Driver assistance')
    # Task2.ICS_ADB_Image_Match_Temp('Test.png', 'Comfort.png')
    # Task2.IC_ADB_Image_Match_Temp('888888888.png', 'test_match.png')
    # Task2.ICS_ADB_Color_Rec('9.png','white.txt')
    # Task2.ICS_ADB_Color_Rec_resourceId('com.nio.settings:id/iv_theme_dark')
    # Task2.IC_ADB_Paddle_OCR('9.png','IC_0517.txt')
    # Task2.Phone_ADB_Paddle_OCR('10.png', '左前门文言cn.txt')
    # Task2.IC_ADB_Image_Match_Temp('9.png','1.png','1.txt')
    # Task2.Cap_log('aaa')
    # Task.Camera_MeterDetection_speed('E:\\01-AZ210262\\10-Python_Project\\Template\\speed_meter.txt')
    # Task.MeterDetection_rpm('E:\\01-AZ210262\\10-Python_Project\\Template\\rpm_meter.txt')
    # Task.Paddle_OCR('E:\\01-AZ210262\\10-Python_Project\\Template\\warning_info.txt')
    # Task2.IC_ADB_Color_Rec('9.png',r'write.txt')

    # Task2.Color_Rec('E:\\01-AZ210262\\10-Python_Project\\Template\\high_beam.txt')
    # Task.Color_Rec('E:\\01-AZ210262\\10-Python_Project\\Template\\high_beam.txt')
    # Task.Freq_Calc(200,None,'E:\\01-AZ210262\\10-Python_Project\\Template\\seatbelt.txt','E:\\01-AZ210262\\10-Python_Project\\Template\\seatbelt.png',100)
    # Task2.Icon_Coord('E:\\01-AZ210262\\10-Python_Project\\ADB_Coord\\Home.txt')
    # Task2.Click_text('Lights')
    # Task2.Click_resourceId('com.nio.settings:id/headlight_mode_auto')
    # Task2.Double_Click('D:\\SoftwareInstall\\TAE3.0.1R_Build20230423\\TAE3.0.1R_Build20230423\\tae_engine\\customlib\\HMI_vue_flask\\hirain-flask-server-master\\HMI_Data\\Image\ROI\\Color\\107.txt')
    # Task2.Swipe_treble('test_icon_1.txt','test_icon_2.txt','test_icon_3.txt')
    Task2.DLT_log_start()
    time.sleep(5)
    Task2.DLT_log_end()
    # Task2.Home()
    # Task2.Back()
    # Task2.ADB_Image_Match_Temp('E:\\01-AZ210262\\10-Python_Project\\ADB_Coord\\Home.png','E:\\01-AZ210262\\10-Python_Project\\ADB_Coord\\Home.txt')
    # for i in range(30):
    #     print(i)
    #     # Task2.ICS_ADB_Paddle_OCR('9.png', 'text.txt')
    #     Task2.ICS_ADB_Paddle_OCR('9.png', '驾驶模式.txt')
    # Task2.Click('Setting.txt')
