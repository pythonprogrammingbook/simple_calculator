from tkinter import *  #导入tkinter模块
import math  #导入math模块
FONT = ('Microsoft YaHei', 12)  #定义字体字号
#定义按键名称
buttons_name = ("%", "CE", "C", "←", "1/x", "x^2", "sqrt", "÷", "7", "8", "9",
                "x", "4", "5", "6", "-", "1", "2", "3", "+", "±", "0", ".", "=")
# 定义计算器GUI页面类
class CalcPage():
    def __init__(self, master):
        self.master = master
        self.calc_flag = False  #检测上一次是否执行了计算
        self.initUI()  #初始化GUI

    def initUI(self):
        '''初始化UI'''
        #计算器结果显示控件
        self.display = StringVar()
        self.result = Entry(self.master,
                            relief=RIDGE,
                            textvariable=self.display,
                            justify='right',
                            font=FONT,
                            bd=5,
                            bg="powder blue")
        self.result.pack(side=TOP, expand=YES, fill=X)
        #设置计算器窗口大小并让其在屏幕居中
        self.center_window()
        #计算器按键都放在Frame中
        self.buttons_frame = Frame(self.master)
        self.buttons_frame.pack(side=BOTTOM, pady=2)
        self.create_buttons(self.click_handler)

    def center_window(self):
        '''让窗口在屏幕上居中'''
        screen_width = self.master.winfo_screenwidth()  #获取屏幕宽度
        screen_height = self.master.winfo_screenheight()  #获取屏幕高度
        x = (screen_width - 200) / 2  #计算窗口坐标x
        y = (screen_height - 100) / 2  #计算窗口坐标y
        self.master.geometry('246x260+%d+%d' % (x, y))  #设置窗口大小与位置
        self.master.title("计算器")  #设置窗口标题

    def create_buttons(self, click_method, names=buttons_name, cols=4):
        '''创建按键并绑定回调函数'''
        for i, name in enumerate(names):
            row, col = i // cols, i % cols
            # 创建按键对象
            b = Button(self.buttons_frame, text=name, font=FONT, width=5)
            b.grid(row=row, column=col)  # 排列按键对象
            b.bind("<Button-1>", click_method)  # 绑定按键回调函数

    def click_handler(self, event):
        '''执行按键功能'''
        c = event.widget["text"]  #获得按键标签
        s = self.display.get()  #获得当前显示
        if "ERROR" in s:
            s = ''
        if c == "←":  #退格键
            self.display.set(s[:-1])
        elif c == "C" or c == "CE":  #清除键
            self.display.set('')
        elif c == "x^2":  #求平方
            self.display.set(eval(s)**2)
        elif c == "sqrt":  #求平方根
            try:
                self.display.set(math.sqrt(eval(s)))
            except:
                self.display.set("ERROR")
        elif c == "1/x":  #求倒数
            try:
                self.display.set(1 / eval(s))
            except:
                self.display.set("ERROR")
        elif c == "±":  #正负号
            if '-' in s:  #若负号已存在
                self.display.set(s[1:])  #去掉负号
            else:  #若负号不存在
                self.display.set('-' + s)  #添加负号
        elif c in "0123456789.":  #数字
            if self.calc_flag:
                self.calc_flag = False
                self.display.set(c)
            else:
                self.display.set(s + c)
        elif c in "+-x÷":  #常规计算符号
            self.display.set(s + c)
        elif c == "=":
            self.calc()
            self.calc_flag = True
        self.result.icursor(len(self.display.get()))

    def calc(self):
        '''执行常规功能计算'''
        try:
            s = self.display.get()
            if "÷" in s:  # 将"÷"替换为"/"
                s = s.replace("÷", "/")
            elif "x" in s:  # 将"x"替换为"*"
                s = s.replace("x", "*")
            self.display.set(eval(s))
        except:
            self.display.set("ERROR")
