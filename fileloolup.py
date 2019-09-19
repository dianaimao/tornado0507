# -*- coding: utf-8 -*-
import os
import sys
import chardet
import time
import re
import random
import logging
import time
from logging import handlers
import glob
from pynput import keyboard
from pynput.keyboard import Key, Listener,Controller
# from pynput.mouse import Controller as MC
Previous_step=''
def main():
    reload(sys)
    sys.setdefaultencoding('gb18030')
    # path=r'D:\test'
    path=r'I:\bug'

    file_list=[]
    file_total=[]
    logger.info('path:   '+path)
    for root, dirs, files in os.walk(path):
        root_list=root.decode('gbk').encode('utf-8')

        for file in files:
            if not file.endswith((r'.jpg','.png','.rar','.torrent','.gif','.xltd','zip')):
                # print file
                file_total.append(os.path.join(root, file))
                if chardet.detect(file)['encoding']=='ascii':
                    file_trasf=file
                    file_list.append(os.path.join(root_list, file_trasf))
                else:
                    file_trasf = file.decode('gbk').encode('utf-8')
                    file_list.append(os.path.join(root_list, file_trasf))

    totalnum=len(file_total)
    logger.info('sum files num:   '+str(totalnum))
    # for i in range(len(file_total)):
    #     #         print file_total[i]
    #     #         print file_list[i]
    randomnum=random.randint(0,totalnum-1)
    logger.info('Its  '+str(randomnum)+'    random file')
    logger.info('Open File Path   '+file_list[randomnum])

    os.startfile(file_total[randomnum])
    return file_total[randomnum]
    # print chardet.detect(os.path.join(root, files[-1]))
    # os.startfile(r'‪D:\迅雷下载\Criminal.Conspiracy.2017.1920X1800.NonDRM_[FHD].mp4')
def produc_press():
    keyboard = Controller()
    # 按键盘和释放键盘
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    # 按小写的a
    keyboard.press('a')
    keyboard.release('a')

    # 按大写的A
    keyboard.press('A')
    keyboard.release('A')


def Log():
    now_time=time.strftime('%Y-%m-%d', time.localtime(time.time()))
    logging.basicConfig(format='%(asctime)s  -  %(levelname)s: -  %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler("log"+time.strftime('%Y-%m-%d',time.localtime(time.time()))+".txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s -  %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def get_key_name(key):
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)
def on_press(key):
    # 监听按键
    if not (key==Key.right or key==Key.left or key==Key.up or key==Key.down or key==Key.enter):
        logger.info('current input:{0} '.format(key))
    if key==Key.end:
        # print('{0} pressed'.format(key))
        global Previous_step
        Previous_step = main()
        logger.info('Previous_step:  '+Previous_step)
        # produc_press()
    if key==Key.home:
        # print 'back_step:'+Previous_step

        os.remove(Previous_step)
        logger.warn('delet file:============='+Previous_step)
if __name__=='__main__':
        # main()
        Log()
        logger = logging.getLogger(__name__)
        logger.info(time.strftime('%Y-%m-%d',time.localtime(time.time())))
        while 1:
            logger.info("===========================================================================")
            logger.info('automatic open file')
            with Listener(on_press=on_press) as listener:
               listener.join()