#-*- coding:utf-8 -*-
# Cube_Timer v0.1.2 --------- by SnapFlip20

import tkinter as tk
from tkinter import messagebox
import datetime, os, time, sys

try:
    sys.path.append("./scr")
except:
    sys.stderr.write('Error: cannot find /scr.\n')
try:
    import genScramble
except ModuleNotFoundError:
    sys.stderr.write('Error: cannot find genScramble.py.\n')
try:
    import showScrambleImg
except ModuleNotFoundError:
    sys.stderr.write('Error: cannot find showScrambleImg.py.\n')

# ---------------------------------------------------------------- #
version = 'v0.1.2'
# ---------------------------------------------------------------- #
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
# ---------------------------------------------------------------- #

def run():
    global time_running, start_time, stop_time, previous_time, elapsed_time

    if time_running:
        mainWindow.bind('<KeyRelease-space>', pause)
        now_time = time.time()
        time_dif = now_time - start_time
        elapsed_time = time_dif + previous_time
        time_txt.configure(text = '{:7.3f}'.format(elapsed_time))
    
    mainWindow.after(1, run)

def scr_refresh(*_): # 스크램블 새로고침
    global scramble_info, scramble_box, scramble_lst,\
        color1, color2, color3, color4, color5, color6, color7, color8, color9,\
            scr_help1, scr_help2
    
    scramble_info = tk.Label(mainWindow, font = ('맑은 고딕', 20), text = 'Scramble')
    scramble_info.place(x = 50, y = 200)

    scramble_box = tk.Text(mainWindow, font = ('맑은 고딕', 15), wrap = 'word', state = 'normal', width = 10)
    scramble_box.place(x = 50, y = 250, width = 350, height = 100)

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
        sys.stderr.write('Error: scramble loading was failed.\n')
        messagebox.showerror(title = 'Exception', message = 'Scramble 을(를) 구성하는 도중 오류가 발생했습니다.')
        sys.exit()
    
    scramble_box.insert(tk.INSERT, scramble_lst)
    scramble_box.configure(state = 'disabled') # 스크램블 박스에 텍스트를 입력할 수 없게 변경

    scr_help1 = tk.Label(mainWindow, font = ('맑은 고딕', 10), text = '윗면이 흰색, 앞면이 초록색인\n상태에서 큐브를 섞어주세요.')
    scr_help1.place(x = 405, y = 185)
    scr_help2 = tk.Label(mainWindow, font = ('맑은 고딕', 10), text = '앞면(초록색)')
    scr_help2.place(x = 457, y = 360)

def start(*_): # 타이머 시작
    global time_running, start_time, stop_time, previous_time, elapsed_time, time_txt

    if not time_running:
        time_running = True
        start_time = time.time()
        previous_time = elapsed_time

def pause(*_): # 타이머 정지
    global time_running, start_time, stop_time, previous_time, elapsed_time, time_txt

    scr_refresh()
    record(str(round(elapsed_time, 3)))
    bundle1()
    mainWindow.bind('<KeyRelease-space>', start)
    time_running = False
    previous_time = elapsed_time = 0.0

def reset(*_): # 타이머 리셋
    global time_running, start_time, stop_time, previous_time, elapsed_time, time_txt

    mainWindow.bind('<KeyRelease-space>', start)
    time_running = False
    elapsed_time = 0.0
    previous_time = 0.0
    time_txt.configure(text = '{:7.3f}'.format(elapsed_time))

def record(t): # 측정된 기록을 record.cbtm 파일에 작성
    farec = open('record.cbtm', 'a')
    farec.write(t + '\n')
    farec.close()

def load_record(): # 최근 기록 표시
    global record_info1,\
        rec1, rec2, rec3, rec4, rec5, rec6, rec7, rec8, rec9, rec10, rec11, rec12
    
    record_info1 = tk.Label(mainWindow, font = ('맑은 고딕 bold', 14), text = '-최근 기록-')
    record_info1.place(x = 448, y = 410)

    rec1 = tk.Text(mainWindow, font = ('맑은 고딕', 15), wrap = 'word', state = 'normal')
    rec1.place(x = 435, y = 450, width = 125, height = 30)
    rec2 = tk.Text(mainWindow, font = ('맑은 고딕', 15), wrap = 'word', state = 'normal')
    rec2.place(x = 435, y = 480, width = 125, height = 30)
    rec3 = tk.Text(mainWindow, font = ('맑은 고딕', 15), wrap = 'word', state = 'normal')
    rec3.place(x = 435, y = 510, width = 125, height = 30)
    rec4 = tk.Text(mainWindow, font = ('맑은 고딕', 15), wrap = 'word', state = 'normal')
    rec4.place(x = 435, y = 540, width = 125, height = 30)
    rec5 = tk.Text(mainWindow, font = ('맑은 고딕', 15), wrap = 'word', state = 'normal')
    rec5.place(x = 435, y = 570, width = 125, height = 30)
    rec6 = tk.Text(mainWindow, font = ('맑은 고딕', 15), wrap = 'word', state = 'normal')
    rec6.place(x = 435, y = 600, width = 125, height = 30)
    rec7 = tk.Text(mainWindow, font = ('맑은 고딕', 15), wrap = 'word', state = 'normal')
    rec7.place(x = 435, y = 630, width = 125, height = 30)
    rec8 = tk.Text(mainWindow, font = ('맑은 고딕', 15), wrap = 'word', state = 'normal')
    rec8.place(x = 435, y = 660, width = 125, height = 30)
    rec9 = tk.Text(mainWindow, font = ('맑은 고딕', 15), wrap = 'word', state = 'normal')
    rec9.place(x = 435, y = 690, width = 125, height = 30)
    rec10 = tk.Text(mainWindow, font = ('맑은 고딕', 15), wrap = 'word', state = 'normal')
    rec10.place(x = 435, y = 720, width = 125, height = 30)
    rec11 = tk.Text(mainWindow, font = ('맑은 고딕', 15), wrap = 'word', state = 'normal')
    rec11.place(x = 435, y = 750, width = 125, height = 30)
    rec12 = tk.Text(mainWindow, font = ('맑은 고딕', 15), wrap = 'word', state = 'normal')
    rec12.place(x = 435, y = 780, width = 125, height = 30)

    try:
        records = []
        frrec = open('record.cbtm', 'r')
        for i in frrec.readlines()[::-1]:
            records.append(i)
        
        if len(records) < 12:
            for i in range(12-len(records)):
                records.append('')
        
        rec1.insert(tk.INSERT, records[0])
        rec1.configure(state = 'disabled')
        rec2.insert(tk.INSERT, records[1])
        rec2.configure(state = 'disabled')
        rec3.insert(tk.INSERT, records[2])
        rec3.configure(state = 'disabled')
        rec4.insert(tk.INSERT, records[3])
        rec4.configure(state = 'disabled')
        rec5.insert(tk.INSERT, records[4])
        rec5.configure(state = 'disabled')
        rec6.insert(tk.INSERT, records[5])
        rec6.configure(state = 'disabled')
        rec7.insert(tk.INSERT, records[6])
        rec7.configure(state = 'disabled')
        rec8.insert(tk.INSERT, records[7])
        rec8.configure(state = 'disabled')
        rec9.insert(tk.INSERT, records[8])
        rec9.configure(state = 'disabled')
        rec10.insert(tk.INSERT, records[9])
        rec10.configure(state = 'disabled')
        rec11.insert(tk.INSERT, records[10])
        rec11.configure(state = 'disabled')
        rec12.insert(tk.INSERT, records[11])
        rec12.configure(state = 'disabled')
        frrec.close()
    except:
        sys.stderr.write('Error: cannot find record.cbtm.\n')
        messagebox.showerror(title = 'Exception', message = '파일 "record.cbtm" 을(를) 찾을 수 없습니다.')
        sys.exit()

def calc5():
    recentAvg5 = []
    farec = open('record.cbtm', 'r')
    cnt = 5
    try:
        for i in farec.readlines()[::-1]:
            if cnt == 0:
                break
            if i == 'DNF':
                recentAvg5.append(0.0)
                continue
            recentAvg5.append(float(i.rstrip()))
            cnt -= 1
        
        if len(recentAvg5) < 5:
            avg5 = 0
        else:
            mn = 1e20
            for i in recentAvg5:
                if i == 'DNF':
                    continue
                mn = min(mn, i)
            mx = -1
            for i in recentAvg5:
                if i == 'DNF':
                    continue
                mx = max(mx, i)
            
            recentAvg5.pop(recentAvg5.index(mn))
            recentAvg5.pop(recentAvg5.index(mx))
            avg5 = sum(recentAvg5)/(3-recentAvg5.count('DNF'))
        
        farec.close()
        return avg5
    except:
        sys.stderr.write('Error: There was an error while calculating recent 5 average.\n')
        messagebox.showerror(title = 'Exception', message = '"record.cbtm" 을(를) 읽는 동안 문제가 발생했습니다.\n파일을 임의로 수정한 적이 있었는지 확인해보십시오.')
        farec.close()
        sys.exit()

def calcAvg5():
    '''
    최근 5회 기록의 평균을 측정하는 함수입니다.
    WCA 규정대로 5회 중 가장 적게 걸린 시간과 가장 많이 걸린 시간을 제외한 뒤
    남은 세 개의 기록으로 평균을 측정합니다.
    '''
    global five_avgtxt

    avg5 = calc5()
    five_avgtxt = tk.Label(mainWindow, font = ('맑은 고딕', 12), text = '· 최근 5회 평균: '+'%.3lf'%avg5)
    five_avgtxt.place(x = 85, y = 575)

def calc12():
    global twelve_avgtxt
    
    recentAvg12 = []
    farec = open('record.cbtm', 'r')
    cnt = 12
    try:
        for i in farec.readlines()[::-1]:
            if cnt == 0:
                break
            if i == 'DNF':
                recentAvg12.append(0.0)
                continue
            recentAvg12.append(float(i.rstrip()))
            cnt -= 1

        if len(recentAvg12) < 12:
            avg12 = 0
        else:
            avg12 = sum(recentAvg12)/(12-recentAvg12.count('DNF'))

        farec.close()
        return avg12
    except:
        sys.stderr.write('Error: There was an error while calculating recent 12 average.\n')
        messagebox.showerror(title = 'Exception', message = '"record.cbtm" 을(를) 읽는 동안 문제가 발생했습니다.\n파일을 임의로 수정한 적이 있었는지 확인해보십시오.')
        farec.close()
        sys.exit()

def calcAvg12():
    '''
    최근 12회 기록의 평균을 측정하는 함수입니다.
    최근 5회 기록의 평균 측정과는 다르게 산술평균을 사용합니다.
    '''
    global twelve_avgtxt
    
    avg12 = calc12()

    twelve_avgtxt = tk.Label(mainWindow, font = ('맑은 고딕', 12), text = '· 최근 12회 평균: '+'%.3lf'%avg12)
    twelve_avgtxt.place(x = 85, y = 600)

def best_score():
    global best_scoretxt

    all_record = []
    farec = open('record.cbtm', 'r')
    try:
        for i in farec.readlines():
            if i == 'DNF':
                continue
            all_record.append(float(i.rstrip()))
        if len(all_record) == 0:
            best = 0
        else:
            best = min(all_record)

        best_scoretxt = tk.Label(mainWindow, font = ('맑은 고딕', 12), text = '· 최고 기록: '+'%.3lf'%best)
        best_scoretxt.place(x = 85, y = 625)
        farec.close()
            
    except:
        sys.stderr.write('Error: There was an error while calculating best score.\n')
        messagebox.showerror(title = 'Exception', message = '"record.cbtm" 을(를) 읽는 동안 문제가 발생했습니다.\n파일을 임의로 수정한 적이 있었는지 확인해보십시오.')
        farec.close()
        sys.exit()

def del_record1():
    try:
        farec = open('record.cbtm', 'r')
        all_record = [i.rstrip() for i in farec.readlines()]
        if len(all_record) == 0:
            return
        all_record.pop()
        farec.close()

        fwrec = open('record.cbtm', 'w')
        for i in all_record:
            fwrec.write(i + '\n')
        fwrec.close()

        bundle1()
    except:
        sys.stderr.write('Error: Cannot delete score.\n')
        messagebox.showerror(title = 'Exception', message = '최근 1회 기록을 삭제할 수 없습니다.')
        farec.close()
        fwrec.close()

def del_record12():
    try:
        farec = open('record.cbtm', 'r')
        all_record = [i.rstrip() for i in farec.readlines()]
        if len(all_record) <= 12:
            del_recordall()
            return
        for i in range(12):
            all_record.pop()
        farec.close()

        fwrec = open('record.cbtm', 'w')
        for i in all_record:
            fwrec.write(i + '\n')
        fwrec.close()

        bundle1()
    except:
        sys.stderr.write('Error: Cannot delete score.\n')
        messagebox.showerror(title = 'Exception', message = '최근 12회 기록을 삭제할 수 없습니다.')
        farec.close()
        fwrec.close()

def del_recordall():
    try:
        farec = open('record.cbtm', 'w')
        farec.close()

        bundle1()
    except:
        sys.stderr.write('Error: Cannot delete score.\n')
        messagebox.showerror(title = 'Exception', message = '모든 기록 삭제를 수행할 수 없습니다.')
        farec.close()

def record_to_txt():
    farec = open('record.cbtm', 'r')
    allRecent = []
    for i in farec.readlines():
        if i == 'DNF':
            allRecent.append(0.0)
            continue
        allRecent.append(float(i.rstrip()))
    
    fwrec = open('record_{}.txt'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')), 'w')
    fwrec.write('\n')
    fwrec.write('======== Cube_Timer record ========\n')
    fwrec.write('파일 저장 시각: {}\n'.format(datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S')))
    fwrec.write('===============================\n')
    fwrec.write('\n')
    for idx, r in enumerate(allRecent):
        fwrec.write(f'{idx+1}. {r}\n')
    fwrec.write('\n')
    fwrec.write('===============================\n')
    fwrec.write('\n')
    fwrec.write(f'최근 5회 평균: {"%.3lf"%calc5()}\n')
    fwrec.write(f'최근 12회 평균: {"%.3lf"%calc12()}\n')
    fwrec.write(f'최고기록: {"%.3lf"%min(allRecent)}\n')
    fwrec.write('\n')

def bundle1(): # 기록 새로고침 관련 함수 모음
    calcAvg5()
    calcAvg12()
    best_score()
    load_record()



class Timer(tk.Frame): # 메인 윈도우 구성
    def __init__(self):
        global mainWindow, time_running, start_time, stop_time, previous_time, elapsed_time,\
            time_txt, logo_image,\
                penalty_bt, penalty_bt_menu, help_bt, recordtxt_bt
        
        mainWindow.title('CubeTimer ' + version)
        time_running = False
        start_time = time.time()
        stop_time = time.time()
        previous_time = 0.0
        elapsed_time = 0.0

        # ---Main UI setting start-----------------------------------------------
        # logo image
        try:
            logo_image = tk.PhotoImage(file = "Cube_Timer_logo.gif")
            logo_show = tk.Label(mainWindow, image = logo_image)
            logo_show.place(x = 20, y = 20)
        except tk.TclError:
            sys.stderr.write('Error: cannot find "Cube_Timer_logo.gif".\n')
            messagebox.showerror(title = 'Exception', message = '파일 "Cube_Timer_logo.gif" 을(를) 찾을 수 없습니다.')
            sys.exit()

        # scramble
        scr_refresh_bt = tk.Button(mainWindow, font = ('맑은 고딕', 12), text = '새로고침', command = scr_refresh)
        scr_refresh_bt.place(x = 300, y = 200, width = 90, height = 40)
        if not time_running:
            scr_refresh()

        # timer
        time_txt = tk.Label(mainWindow, text = '0.000', font = ('consolas 35 bold'))
        time_txt.place(x = 120, y = 450)
        mainWindow.bind('<KeyRelease-space>', start)
        reset()

        time_info = tk.Label(mainWindow, font = ('맑은 고딕', 14), text = '시작하거나 멈추려면 Space키를 누르세요.')
        time_info.place(x = 51, y = 525)

        # stat
        bundle1()

        # button
        penalty_bt = tk.Menubutton(mainWindow, font = ('맑은 고딕', 12), text = '기록 수정하기', relief = 'raised', direction = 'below')
        penalty_bt.place(x = 70, y = 700, width = 150, height = 70)
        penalty_bt_menu = tk.Menu(penalty_bt, tearoff = 0)
        penalty_bt_menu.add_command(label = '최근 기록 1회 삭제', command = del_record1)
        penalty_bt_menu.add_command(label = '최근 기록 12회 삭제', command = del_record12)
        penalty_bt_menu.add_command(label = '최근 기록 모두 삭제', command = del_recordall)
        penalty_bt_menu.add_separator()
        penalty_bt_menu.add_command(label = '최근 기록 1회 DNF 처리', command = comming_soon)
        penalty_bt_menu.add_command(label = '최근 기록에 2초 Penalty 추가', command = comming_soon)
        penalty_bt_menu.add_command(label = '최근 기록에 2초 Penalty 삭제', command = comming_soon)
        penalty_bt["menu"] = penalty_bt_menu

        help_bt = tk.Button(mainWindow, font = ('맑은 고딕', 12), text = '도움말', command = help_win)
        help_bt.place(x = 240, y = 700, width = 150, height = 70)

        recordtxt_bt = tk.Button(mainWindow, font = ('맑은 고딕', 11), text = '텍스트 파일로 저장', command = record_to_txt)
        recordtxt_bt.place(x = 427, y = 825, width = 140, height = 30)
        # ---Main UI setting end-----------------------------------------------

        sys.stdout.write('Timer.__init__() is executed.\n')

    def _debug(self):
        global time_running, start_time, stop_time, previous_time, elapsed_time, time_txt
        print('이 문장이 출력이 되나요?')
        print(time_running)



def help_win():
    global help_txt1
    helpWindow = tk.Tk()
    helpWindow.geometry("400x600")
    helpWindow.resizable(width = False, height = False)
    help_txt1 = tk.Label(helpWindow, font = ('맑은 고딕', 12), text = '업데이트 예정입니다.')
    help_txt1.place(x = 125, y = 200)
    helpWindow.mainloop()

def comming_soon():
    messagebox.showinfo(title = '알림', message = '업데이트 예정입니다.')



if __name__ == "__main__":
    mainWindow = tk.Tk()
    mainWindow.geometry("600x900+100-100")
    mainWindow.resizable(width = False, height = False)

    pusher()
    Timer()
    load_record()
    run()
    mainWindow.mainloop()
    
    
    
