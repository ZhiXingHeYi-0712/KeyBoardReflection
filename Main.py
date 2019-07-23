from pynput.keyboard import *
from pynput.keyboard import KeyCode
from win32api import ShellExecute

class Otherkey():
    NONE_KEY = KeyCode.from_vk(255) # 把Calculator键映射到了255位置

def on_release(key):
    ' 释放检测 '
    if (key == Otherkey.NONE_KEY):
        ShellExecute(0,'open','C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe', '','',1)

with Listener(on_release=on_release) as listener:
    # 维持运行必备
    listener.join()