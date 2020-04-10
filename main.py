import tkinter as tk  #导入tkinter模块
from calculator.simple_ui import *  #导入自定义用户界面模块

window = tk.Tk()      #创建主窗口对象 
CalcPage(window)      #创建计算器页面
window.mainloop()     #启动tkinter主循环
