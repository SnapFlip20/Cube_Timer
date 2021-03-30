#-*- coding:utf-8 -*-
# Cube_Timer v0.0.1 --------- SnapFlip20

import tkinter as tk
from tkinter import messagebox
import os, time, sys

sys.path.append("./scr")
import genScramble

def run():
    global mainWindow, time_running, start_time, stop_time, previous_time, elapsed_time
    if time_running:
        mainWindow.bind('<KeyRelease-space>', pause)
        now_time = time.time()
        time_dif = now_time - start_time
        elapsed_time = time_dif + previous_time
        time_txt.configure(text = '{:7.3f}'.format(elapsed_time))
    
    mainWindow.after(10, run)

def start(*_):
    global time_running, start_time, stop_time, previous_time, elapsed_time, time_txt
    if not time_running:
        time_running = True
        start_time = time.time()
        previous_time = elapsed_time
def pause(*_):
    global time_running, start_time, stop_time, previous_time, elapsed_time, time_txt
    mainWindow.bind('<KeyRelease-space>', reset)
    time_running = False
    previous_time = elapsed_time
def reset(*_):
    global time_running, start_time, stop_time, previous_time, elapsed_time, time_txt
    mainWindow.bind('<KeyRelease-space>', start)
    time_running = False
    elapsed_time = 0.0
    previous_time = 0.0
    time_txt.configure(text = '{:7.3f}'.format(elapsed_time))

class Timer(tk.Frame):
    def __init__(self):
        global mainWindow, time_running, start_time, stop_time, previous_time, elapsed_time,\
            time_txt, logo_image,\
                color1, color2, color3, color4, color5, color6, color7, color8, color9
        
        mainWindow.title('CubeTimer v0.0.1')
        time_running = False
        start_time = time.time()
        stop_time = time.time()
        previous_time = 0.0
        elapsed_time = 0.0

        # ---Main UI Setting start----------------------------
        # logo image
        try:
            logo_image = tk.PhotoImage(file = "Cube_Timer_logo.gif")
            logo_show = tk.Label(mainWindow, image = logo_image)
            logo_show.place(x = 20, y = 20)
        except tk.TclError:
            sys.stderr.write('cannot find "Cube_Timer_logo.gif".\n')
            messagebox.showerror(title = 'Exception', message = '파일 "Cube_Timer_logo.gif" 을(를) 찾을 수 없습니다.')
            sys.exit()

        # scramble
        # 스크램블 박스 그냥 텍스트로 바꾸기!!
        scramble_info = tk.Label(mainWindow, font = ('나눔고딕', 20), text = 'Scramble')
        scramble_info.place(x = 50, y = 200)
        scramble_refresh = False # 임시

        #scramble_box = tk.Entry(mainWindow, font = ('나눔고딕', 20), relief = 'solid')
        scramble_box = tk.Text(mainWindow, font = ('나눔고딕 bold', 15), wrap = 'word', state = 'normal', width = 10)
        scramble_box.place(x = 50, y = 250, width = 350, height = 100)

        try:
            scramble_lst = genScramble.gen_scramble()
            #print(scramble_lst)
            color1 = tk.PhotoImage(file = "image/{}".format('default'+'.gif'))
            colorf1 = tk.Label(mainWindow, image = color1)
            colorf1.place(x = 430, y = 230)
            color2 = tk.PhotoImage(file = "image/{}".format('default'+'.gif'))
            colorf2 = tk.Label(mainWindow, image = color2)
            colorf2.place(x = 475, y = 230)
            color3 = tk.PhotoImage(file = "image/{}".format('default'+'.gif'))
            colorf3 = tk.Label(mainWindow, image = color3)
            colorf3.place(x = 520, y = 230)
            color4 = tk.PhotoImage(file = "image/{}".format('default'+'.gif'))
            colorf4 = tk.Label(mainWindow, image = color4)
            colorf4.place(x = 430, y = 275)
            color5 = tk.PhotoImage(file = "image/{}".format('default'+'.gif'))
            colorf5 = tk.Label(mainWindow, image = color5)
            colorf5.place(x = 475, y = 275)
            color6 = tk.PhotoImage(file = "image/{}".format('default'+'.gif'))
            colorf6 = tk.Label(mainWindow, image = color6)
            colorf6.place(x = 520, y = 275)
            color7 = tk.PhotoImage(file = "image/{}".format('default'+'.gif'))
            colorf7 = tk.Label(mainWindow, image = color7)
            colorf7.place(x = 430, y = 320)
            color8 = tk.PhotoImage(file = "image/{}".format('default'+'.gif'))
            colorf8 = tk.Label(mainWindow, image = color8)
            colorf8.place(x = 475, y = 320)
            color9 = tk.PhotoImage(file = "image/{}".format('default'+'.gif'))
            colorf9 = tk.Label(mainWindow, image = color9)
            colorf9.place(x = 520, y = 320)
        except:
            sys.stderr.write('cannot find color image.\n')
            messagebox.showerror(title = 'Exception', message = 'color image 을(를) 찾을 수 없습니다.')
            sys.exit()
        scramble_box.insert(tk.INSERT, scramble_lst)
        scramble_box.configure(state = 'disabled')

        # timer
        time_txt = tk.Label(mainWindow, text = '0.000', font = ('consolas 35 bold'))
        time_txt.place(x = 120, y = 450)
        mainWindow.bind('<KeyRelease-space>', start)
        reset()

        time_info = tk.Label(mainWindow, font = ('나눔고딕', 15), text = '시작하거나 멈추려면 Space키를 누르세요')
        time_info.place(x = 55, y = 550)
        

        # ---Main UI Setting end----------------------------

        print('Timer.__init__() is executed.')
        

    def _debug(self):
        global time_running, start_time, stop_time, previous_time, elapsed_time, time_txt
        print('이 문장이 출력이 되나요?')
        print(time_running)

def debug():
    None

if __name__ == "__main__":
    mainWindow = tk.Tk()
    mainWindow.geometry("600x900+200+100")
    mainWindow.resizable(width = False, height = False)

    Timer()
    run()
    mainWindow.mainloop()
    
    
    
