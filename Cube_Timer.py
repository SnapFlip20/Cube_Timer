#-*- coding:utf-8 -*-
# Cube_Timer v0.0.4 --------- SnapFlip20

import tkinter as tk
from tkinter import messagebox
import os, time, sys

sys.path.append("./scr")
import genScramble, showScrambleImg

version = 'v0.0.4'

def pusher(): # batch file generator for Github push
    fbat = open('push.bat', 'w')
    fbat.write('@echo off\n')
    fbat.write('title git_push_program\n')
    fbat.write('mode con cols=100 lines=30\n')
    fbat.write(':main\n')
    fbat.write('git add .\n')
    fbat.write('git commit -m "CubeTimer_{}"\n'.format(version))
    fbat.write('git push\n')
    fbat.write('echo done\n')
    fbat.write('pause>nul\n')
    fbat.close()

def run():
    global mainWindow, time_running, start_time, stop_time, previous_time, elapsed_time
    if time_running:
        mainWindow.bind('<KeyRelease-space>', pause)
        now_time = time.time()
        time_dif = now_time - start_time
        elapsed_time = time_dif + previous_time
        time_txt.configure(text = '{:7.3f}'.format(elapsed_time))
    
    mainWindow.after(10, run)

def scr_refresh(*_):
    global scramble_info, scramble_box, scramble_lst, scr_refresh_bt,\
        color1, color2, color3, color4, color5, color6, color7, color8, color9,\
            scr_help1, scr_help2
    
    scramble_info = tk.Label(mainWindow, font = ('나눔고딕', 20), text = 'Scramble')
    scramble_info.place(x = 50, y = 200)

    scramble_box = tk.Text(mainWindow, font = ('나눔고딕 bold', 15), wrap = 'word', state = 'normal', width = 10)
    scramble_box.place(x = 50, y = 250, width = 350, height = 100)

    if time_running:
        reset()

    try:
        scramble_lst = genScramble.gen_scramble()
        scr_result = showScrambleImg.return_color(scramble_lst)
        color1 = tk.PhotoImage(file = "image/{}".format(scr_result[0]+'.gif'))
        colorf1 = tk.Label(mainWindow, image = color1)
        colorf1.place(x = 430, y = 230)
        color2 = tk.PhotoImage(file = "image/{}".format(scr_result[1]+'.gif'))
        colorf2 = tk.Label(mainWindow, image = color2)
        colorf2.place(x = 475, y = 230)
        color3 = tk.PhotoImage(file = "image/{}".format(scr_result[2]+'.gif'))
        colorf3 = tk.Label(mainWindow, image = color3)
        colorf3.place(x = 520, y = 230)
        color4 = tk.PhotoImage(file = "image/{}".format(scr_result[3]+'.gif'))
        colorf4 = tk.Label(mainWindow, image = color4)
        colorf4.place(x = 430, y = 275)
        color5 = tk.PhotoImage(file = "image/{}".format(scr_result[4]+'.gif'))
        colorf5 = tk.Label(mainWindow, image = color5)
        colorf5.place(x = 475, y = 275)
        color6 = tk.PhotoImage(file = "image/{}".format(scr_result[5]+'.gif'))
        colorf6 = tk.Label(mainWindow, image = color6)
        colorf6.place(x = 520, y = 275)
        color7 = tk.PhotoImage(file = "image/{}".format(scr_result[6]+'.gif'))
        colorf7 = tk.Label(mainWindow, image = color7)
        colorf7.place(x = 430, y = 320)
        color8 = tk.PhotoImage(file = "image/{}".format(scr_result[7]+'.gif'))
        colorf8 = tk.Label(mainWindow, image = color8)
        colorf8.place(x = 475, y = 320)
        color9 = tk.PhotoImage(file = "image/{}".format(scr_result[8]+'.gif'))
        colorf9 = tk.Label(mainWindow, image = color9)
        colorf9.place(x = 520, y = 320)
    except:
        sys.stderr.write('cannot find color image.\n')
        messagebox.showerror(title = 'Exception', message = 'color image 을(를) 찾을 수 없습니다.')
        sys.exit()
    scramble_box.insert(tk.INSERT, scramble_lst)
    scramble_box.configure(state = 'disabled') # 스크램블 박스에 텍스트를 입력할 수 없게 변경

    scr_help1 = tk.Label(mainWindow, font = ('나눔고딕', 11), text = '윗면이 흰색, 앞면이 초록색인\n상태에서 큐브를 섞어주세요.')
    scr_help1.place(x = 403, y = 185)
    scr_help2 = tk.Label(mainWindow, font = ('나눔고딕', 10), text = '앞면(초록색)')
    scr_help2.place(x = 460, y = 360)

def start(*_):
    global time_running, start_time, stop_time, previous_time, elapsed_time, time_txt
    if not time_running:
        time_running = True
        start_time = time.time()
        previous_time = elapsed_time

def pause(*_):
    global time_running, start_time, stop_time, previous_time, elapsed_time, time_txt
    scr_refresh()
    mainWindow.bind('<KeyRelease-space>', start)
    time_running = False
    previous_time = elapsed_time = 0.0


def reset(*_):
    global time_running, start_time, stop_time, previous_time, elapsed_time, time_txt
    mainWindow.bind('<KeyRelease-space>', start)
    time_running = False
    elapsed_time = 0.0
    previous_time = 0.0
    time_txt.configure(text = '{:7.3f}'.format(elapsed_time))


def record_list():
    global rec1



class Timer(tk.Frame):
    def __init__(self):
        global mainWindow, time_running, start_time, stop_time, previous_time, elapsed_time,\
            time_txt, logo_image
        
        mainWindow.title('CubeTimer ' + version)
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
        # TODO: 설명 추가 -> 윗면을 흰색, 앞면을 빨간색으로 한 뒤 섞으시오
        scr_refresh_bt = tk.Button(mainWindow, font = ('나눔고딕', 12), text = '새로고침', command = scr_refresh)
        scr_refresh_bt.place(x = 300, y = 200, width = 90, height = 40)
        scr_refresh()

        # timer
        time_txt = tk.Label(mainWindow, text = '0.000', font = ('consolas 35 bold'))
        time_txt.place(x = 120, y = 450)
        mainWindow.bind('<KeyRelease-space>', start)
        reset()

        time_info = tk.Label(mainWindow, font = ('나눔고딕', 15), text = '시작하거나 멈추려면 Space키를 누르세요')
        time_info.place(x = 55, y = 550)

        # 
        # ---Main UI Setting end----------------------------

        print('Timer.__init__() is executed.')
        

    def _debug(self):
        global time_running, start_time, stop_time, previous_time, elapsed_time, time_txt
        print('이 문장이 출력이 되나요?')
        print(time_running)



if __name__ == "__main__":
    mainWindow = tk.Tk()
    mainWindow.geometry("600x900+200+100")
    mainWindow.resizable(width = False, height = False)

    pusher()
    Timer()
    run()
    mainWindow.mainloop()
    
    
    
