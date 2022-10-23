import datetime
import json
import os.path

import pyautogui
import win32con,time
import win32api
from pyperclip import copy as pycopy
from PIL import ImageGrab

def ctrl_v():
    win32api.keybd_event(17, 0, 0, 0)  # Ctrl
    win32api.keybd_event(86, 0, 0, 0)  # V
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放指令
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

def tab(times):
    for i in range(times):
        win32api.keybd_event(9, 0, 0, 0)  # Tab
        win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.5)

def delete(times):
    for i in range(times):
        win32api.keybd_event(8, 0, 0, 0)  # Tab
        win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.05)



def read_file():
    f=open('name_id','r',encoding='utf-8')
    person_dict={}
    f1=f.readline()
    i=1
    location=0
    while f1:
        try:
            int(f1[3])
            location =3
        except ValueError as e:
            print(str(e))
            location = 2
        name=f1[0:location]
        id=f1[location:]
        person_dict[i]={
            'name':name,
            'id':id.replace('\n','')
        }
        i+=1
        f1=f.readline()
    f.close()
    return person_dict



person_dict=read_file()

def grab(name):
    im = ImageGrab.grab(bbox =(852, 4, 1708, 1508))
    path_name = datetime.datetime.now().strftime('%Y-%m-%d')
    if not os.path.exists(path_name):
        os.mkdir(path_name)
    im.save(os.path.join(path_name,name+'.png'), 'png')

for k,v in person_dict.items():
    time.sleep(3)
    pyautogui.moveTo(1225, 364)
    pyautogui.click()
    delete(5)
    pycopy(v['name'])
    print(v['name'])
    ctrl_v()
    tab(1)
    delete(20)
    pycopy(v['id'])
    print(v['id'])
    ctrl_v()
    pyautogui.moveTo(1225, 664)
    pyautogui.click()
    time.sleep(3)
    grab(v['name'])



























