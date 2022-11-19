#-*- coding:utf-8 -*-
# Cube_Timer v0.2.0 --------- by SnapFlip20

import tkinter as tk
from tkinter import messagebox, scrolledtext
import datetime, os, time, statistics, sys

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
version = 'v0.2.0'
# -push.bat------------------------------------------------------- #
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
        time_txt.configure(fg = 'black')
        mainWindow.bind('<KeyRelease-space>', pause)
        now_time = time.time()
        time_dif = now_time - start_time
        elapsed_time = time_dif + previous_time
        time_txt.configure(text = f'{time_converter(elapsed_time)}')
    
    mainWindow.after(10, run)



def scr_refresh(*_):
    '''
    genScramble.py에서 랜덤으로 생성된 스크램블을 텍스트로 출력하고,
    스크램블 후 윗면의 모습을 이미지로 표시합니다.
    '''
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
    scramble_box.configure(state = 'disabled')

    scr_help1 = tk.Label(mainWindow, font = ('맑은 고딕', 10), text = '윗면이 흰색, 앞면이 초록색인\n상태에서 큐브를 섞어주세요.')
    scr_help1.place(x = 405, y = 185)
    scr_help2 = tk.Label(mainWindow, font = ('맑은 고딕', 10), text = '앞면(초록색)')
    scr_help2.place(x = 457, y = 360)

def start(*_): # 타이머 시작
    global time_running, start_time, stop_time, previous_time, elapsed_time, time_txt, now_scr
    now_scr = scramble_lst
    if not time_running:
        time_running = True
        start_time = time.time()
        previous_time = elapsed_time

def pause(*_): # 타이머 정지
    global time_running, start_time, stop_time, previous_time, elapsed_time, time_txt

    time_txt.configure(fg = 'limegreen')
    scr_refresh()
    record(str(round(elapsed_time, 3)))
    record_new(str(round(elapsed_time, 3)), now_scr, 0)
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
    time_txt.configure(text = '0:00.000')

def record(t): # 측정된 기록을 record.cbtm 파일에 작성
    farec = open('record.cbtm', 'a')
    farec.write(t + '\n')
    farec.close()

def record_new(t, sc, isP):
    nowtime = datetime.datetime.now().strftime("%Y %m %d %H %M %S")
    nowtime_lst = list(nowtime.split())
    farec = open('recordDB.cbtm', 'a')
    farec.write(f'{t} {sc} {nowtime_lst} {isP}\n')
    farec.close()

def load_record():
    '''
    최근 측정한 12회 기록을 측정 시기가 빠른 기록 순으로 표시합니다.
    '''
    global record_info1,\
        rec1, rec2, rec3, rec4, rec5, rec6, rec7, rec8, rec9, rec10, rec11, rec12
    
    record_info1 = tk.Label(mainWindow, font = ('맑은 고딕 bold', 14), text = '-최근 기록-')
    record_info1.place(x = 445, y = 410)

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
            records.append(time_converter(float(i)))
        
        if len(records) < 12:
            for i in range(12-len(records)):
                records.append('')
        
        for (i, j) in enumerate(records):
            if j.rstrip() == '0':
                records[i] = 'DNF'
        
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

def time_converter(s): # ms 단위의 시간을 h:s:m.ms 단위로 변환하여 표시
    ms = round(s - int(s), 3)
    s = int(s)
    h = s//3600
    s = s - h*3600
    m = s//60
    s = s - m*60
    h = str(h); m = str(m); s = str(s); ms = str(ms)[2:]
    #return f'{h}:{m}:{s}.{ms}'
    return f'{m}:{s.zfill(2)}.{ms.zfill(3)}'

def calc5():
    '''
    최근 5회 기록의 평균을 측정하는 함수입니다.
    5회 기록 중 최고 기록과 최저 기록을 제외한
    3개의 기록으로 평균을 측정합니다.
    DNF가 2개 이상일 경우 평균이 DNF로 표시됩니다.
    '''
    recentAvg5 = []
    farec = open('record.cbtm', 'r')
    try:
        recentAvg5 = list(map(float, farec.readlines()[::-1][:5]))
        if recentAvg5.count(0) > 1:
            avg5 = 'DNF'
        else:
            if len(recentAvg5) < 5:
                avg5 = 0
            else:
                recentAvg5.sort()
                avg5 = statistics.mean(recentAvg5[1:-1])
        farec.close()
        return avg5
    except:
        sys.stderr.write('Error: There was an error while calculating recent 5 average.\n')
        messagebox.showerror(title = 'Exception', message = '"record.cbtm" 을(를) 읽는 동안 문제가 발생했습니다.\n파일을 임의로 수정한 적이 있었는지 확인해보십시오.')
        farec.close()
        sys.exit()

def calcAvg5():
    global five_avgtxt

    avg5 = calc5()
    if avg5 == 'DNF':
        five_avgtxt = tk.Label(mainWindow, font = ('맑은 고딕', 12), text = '· 최근 5회 평균: D N F     ')
    else:
        five_avgtxt = tk.Label(mainWindow, font = ('맑은 고딕', 12), text = '· 최근 5회 평균: '+'%.3lf'%avg5+'     ')
    five_avgtxt.place(x = 85, y = 575)

def calc12():
    '''
    최근 12회 기록의 평균을 측정하는 함수입니다.
    12회 기록 중 최고 기록과 최저 기록을 제외한
    10개의 기록으로 평균을 측정합니다.
    DNF가 2개 이상일 경우 평균이 DNF로 표시됩니다.
    '''
    recentAvg12 = []
    farec = open('record.cbtm', 'r')
    try:
        recentAvg12 = list(map(float, farec.readlines()[::-1][:12]))
        if recentAvg12.count(0) > 1:
            avg12 = 'DNF'
        else:
            if len(recentAvg12) < 12:
                avg12 = 0
            else:
                recentAvg12.sort()
                avg12 = statistics.mean(recentAvg12[1:-1])
        farec.close()
        return avg12
    except:
        sys.stderr.write('Error: There was an error while calculating recent 12 average.\n')
        messagebox.showerror(title = 'Exception', message = '"record.cbtm" 을(를) 읽는 동안 문제가 발생했습니다.\n파일을 임의로 수정한 적이 있었는지 확인해보십시오.')
        farec.close()
        sys.exit()

def calcAvg12():
    global twelve_avgtxt

    avg12 = calc12()
    if avg12 == 'DNF':
        twelve_avgtxt = tk.Label(mainWindow, font = ('맑은 고딕', 12), text = '· 최근 12회 평균: D N F     ')
    else:
        twelve_avgtxt = tk.Label(mainWindow, font = ('맑은 고딕', 12), text = '· 최근 12회 평균: '+'%.3lf'%avg12+'     ')
    twelve_avgtxt.place(x = 85, y = 600)

def calcAvgall():
    '''
    측정된 모든 기록의 산술평균을 측정하는 함수입니다.
    DNF가 2개 이상일 경우 평균이 DNF로 표시됩니다.
    '''
    global all_avgtxt

    all_record = []
    farec = open('record.cbtm', 'r')
    try:
        all_record = list(map(float, farec.readlines()))
        if all_record.count(0) > 1:
            avgall = 'DNF'
        else:
            if len(all_record) == 0:
                avgall = 0
            else:
                if 0 in all_record:
                    if len(all_record) == 1:
                        avgall = 0
                    else:
                        avgall = sum(all_record)/(len(all_record)-1)
                else:
                    avgall = statistics.mean(all_record)
        farec.close()

        if avgall == 'DNF':
            all_avgtxt = tk.Label(mainWindow, font = ('맑은 고딕', 12), text = '· 전체 평균: D N F     ')
        else:
            all_avgtxt = tk.Label(mainWindow, font = ('맑은 고딕', 12), text = '· 전체 평균: '+'%.3lf'%avgall+'     ')
        all_avgtxt.place(x = 85, y = 625)
    except:
        sys.stderr.write('Error: There was an error while calculating all average.\n')
        messagebox.showerror(title = 'Exception', message = '"record.cbtm" 을(를) 읽는 동안 문제가 발생했습니다.\n파일을 임의로 수정한 적이 있었는지 확인해보십시오.')
        farec.close()
        sys.exit()

def best_score():
    '''
    최고 기록을 측정하는 함수입니다.
    DNF가 1개일 경우 DNF를 제외한 최고 기록이 표시됩니다.
    DNF가 2개 이상일 경우 최고 기록이 DNF로 표시됩니다.
    '''
    global best_scoretxt

    all_record = []
    farec = open('record.cbtm', 'r')
    try:
        all_record = []
        farec = open('record.cbtm', 'r')
        all_record = list(map(float, farec.readlines()))
        if all_record.count(0) > 1:
            best = 'DNF'
        else:
            if len(all_record) == 0:
                best = 0
            elif len(all_record) == 1:
                best = all_record[0]
            else:
                all_record.sort()
                best = all_record[1] if all_record[0] == 0 else all_record[0]
        if best == 'DNF':
            best_scoretxt = tk.Label(mainWindow, font = ('맑은 고딕', 12), text = '· 최고 기록: D N F     ')
        else:
            best_scoretxt = tk.Label(mainWindow, font = ('맑은 고딕', 12), text = '· 최고 기록: '+'%.3lf'%best+'     ')
        best_scoretxt.place(x = 85, y = 650)
        farec.close()
            
    except:
        sys.stderr.write('Error: There was an error while calculating best score.\n')
        messagebox.showerror(title = 'Exception', message = '"record.cbtm" 을(를) 읽는 동안 문제가 발생했습니다.\n파일을 임의로 수정한 적이 있었는지 확인해보십시오.')
        farec.close()
        sys.exit()

def del_record1(): # 최근 기록 1회 삭제
    try:
        farec = open('record.cbtm', 'r')
        all_record = [i.rstrip() for i in farec.readlines()]
        if len(all_record) == 0:
            messagebox.showerror(title = 'Error', message = '삭제할 기록이 없습니다.')
            return
        all_record.pop()
        farec.close()

        ask_delrec1 = messagebox.askquestion(title = '알림', message = '최근 기록 1회를 삭제하시겠습니까?')
        if ask_delrec1 == 'yes':
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

def del_record12(): # 최근 기록 12회 삭제
    try:
        farec = open('record.cbtm', 'r')
        all_record = [i.rstrip() for i in farec.readlines()]
        if len(all_record) == 0:
            messagebox.showerror(title = 'Error', message = '삭제할 기록이 없습니다.')
            return
        if len(all_record) <= 12:
            del_recordall(2)
            return
        else:
            for i in range(12):
                all_record.pop()
            farec.close()

            ask_delrec12 = messagebox.askquestion(title = '알림', message = '최근 기록 12회를 삭제하시겠습니까?')
            if ask_delrec12 == 'yes':
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

def del_recordall(case=1): # 측정된 모든 기록 삭제
    try:
        if case == 1:
            ask_delrecall = messagebox.askquestion(title = '알림', message = '측정된 모든 기록을 삭제하시겠습니까?')
            if ask_delrecall == 'yes':
                farec = open('record.cbtm', 'w')
                farec.close()
                bundle1()
        elif case == 2:
            ask_delrec12 = messagebox.askquestion(title = '알림', message = '최근 기록 12회를 삭제하시겠습니까?')
            if ask_delrec12 == 'yes':
                farec = open('record.cbtm', 'w')
                farec.close()
                bundle1()
    except:
        sys.stderr.write('Error: Cannot delete score.\n')
        messagebox.showerror(title = 'Exception', message = '모든 기록 삭제를 수행할 수 없습니다.')
        farec.close()

def dnf_add(): # 최근 기록에 DNF 추가
    try:
        farec = open('record.cbtm', 'r')
        all_record = [i.rstrip() for i in farec.readlines()]
        farec.close()

        if len(all_record) == 0:
            messagebox.showerror(title = 'Exception', message = 'DNF 처리할 기록이 없습니다.')
        elif all_record[-1] == '0':
            messagebox.showerror(title = 'Exception', message = '이미 DNF 처리된 기록입니다.')
        else:
            ask_dnfadd = messagebox.askquestion(title = '알림', message = f'최근 기록({all_record[-1]})을 DNF 처리하시겠습니까?\n이 작업은 되돌릴 수 없습니다.')
            if ask_dnfadd == 'yes':
                all_record[-1] = '0'

        fwrec = open('record.cbtm', 'w')
        for i in all_record:
            fwrec.write(i + '\n')
        fwrec.close()

        bundle1()
    except:
        sys.stderr.write('Error: Cannot add DNF.\n')
        messagebox.showerror(title = 'Exception', message = 'DNF 처리하는 과정에서 문제가 발생했습니다.')

def change_txtcol(*_):
    if not time_running:
        time_txt.configure(text = '0:00.000', fg = 'red')

def bundle1(): # 기록 새로고침 관련 함수 모음
    calcAvg5()
    calcAvg12()
    calcAvgall()
    best_score()
    load_record()



# -mainUI--------------------------------------------------------- #
class Timer(tk.Frame): # 메인 윈도우 구성
    def __init__(self):
        global mainWindow, time_running, start_time, stop_time, previous_time, elapsed_time,\
            time_txt, logo_image,\
                penalty_bt, penalty_bt_menu, help_bt, statis_bt, setting_bt
        
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
        time_txt = tk.Label(mainWindow, text = '0:00:00', font = ('consolas 32 bold'))
        time_txt.place(x = 140, y = 440)
        mainWindow.bind('<space>', change_txtcol)
        mainWindow.bind('<KeyRelease-space>', start)
        time_txt.configure(text = '0:00:00', fg = 'black')
        reset()

        time_info = tk.Label(mainWindow, font = ('맑은 고딕', 14), text = '시작하거나 멈추려면 Space키를 누르세요.')
        time_info.place(x = 51, y = 525)

        # stat
        bundle1()

        # button
        penalty_bt = tk.Menubutton(mainWindow, font = ('맑은 고딕', 12), text = '기록 수정하기', relief = 'raised', direction = 'below')
        penalty_bt.place(x = 60, y = 700, width = 160, height = 70)
        penalty_bt_menu = tk.Menu(penalty_bt, tearoff = 0)
        penalty_bt_menu.add_command(label = '최근 기록 1회 삭제', command = del_record1)
        penalty_bt_menu.add_command(label = '최근 기록 12회 삭제', command = del_record12)
        penalty_bt_menu.add_command(label = '최근 기록 모두 삭제', command = del_recordall)
        penalty_bt_menu.add_separator()
        penalty_bt_menu.add_command(label = '최근 기록 1회 DNF 처리', command = dnf_add)
        penalty_bt_menu.add_command(label = '최근 기록 1회 2초 패널티 추가', command = comming_soon)
        penalty_bt["menu"] = penalty_bt_menu

        help_bt = tk.Button(mainWindow, font = ('맑은 고딕', 12), text = '도움말', command = help_win)
        help_bt.place(x = 240, y = 700, width = 160, height = 70)

        statis_bt = tk.Button(mainWindow, font = ('맑은 고딕', 12), text = '통계', command = comming_soon)
        statis_bt.place(x = 240, y = 775, width = 160, height = 35)

        setting_bt = tk.Button(mainWindow, font = ('맑은 고딕', 12), text = '설정', command = comming_soon) 
        setting_bt.place(x = 240, y = 815, width = 160, height = 35)

        # ---Main UI setting end-----------------------------------------------



def help_win():
    global help_txt1
    helpWindow = tk.Tk()
    helpWindow.geometry("400x600")
    helpWindow.resizable(width = False, height = False)
    #help_txt1 = tk.Label(helpWindow, font = ('맑은 고딕', 12), text = '업데이트 예정입니다.\n\n제작자: SnapFlip20')
    #help_txt1.place(x = 125, y = 200)
    help_txt = scrolledtext.ScrolledText(helpWindow, width = 40, height = 25, font = ('맑은 고딕', 12))
    help_txt.insert(tk.END, f'Cube Timer {version}\n\n')
    help_txt.insert(tk.END, '※ 기록 측정 방법:\n')
    help_txt.insert(tk.END, '· 스페이스 바를 눌렀다가 떼는 순간 타이머가 시작됩니다.\n')
    help_txt.insert(tk.END, '· 스페이스 바를 다시 누르면 타이머가 정지되고 측정된 기록이 저장됩니다.\n')
    help_txt.insert(tk.END, '· 우측 -최근 기록- 에서 저장된 기록들을 확인할 수 있으며, 측정 일시가 빠른 순으로 표시됩니다.\n')
    help_txt.insert(tk.END, '· 최근 기록 1회, 12회, 전체를 삭제할 수 있으며, 이 작업은 되돌릴 수 없습니다.\n')
    help_txt.insert(tk.END, '· 최근 기록 1회에 대해서 DNF와 2초 패널티를 적용할 수 있으며, 이 작업은 되돌릴 수 없습니다.\n\n')
    help_txt.insert(tk.END, '※ 기록 측정 방식\n')
    help_txt.insert(tk.END, '· DNF가 2회 이상일 경우 5회, 12회, 전체 평균, 최고 기록이 모두 DNF로 표시됩니다.\n')
    help_txt.insert(tk.END, '\n')
    help_txt.insert(tk.END, '\n')
    help_txt.insert(tk.END, '\n')
    help_txt.insert(tk.END, '제작자: SnapFlip20\n')
    help_txt.insert(tk.END, 'https://github.com/SnapFlip20/Cube_Timer\n')
    help_txt.configure(state = 'disabled')
    help_txt.pack()
    helpWindow.mainloop()

def comming_soon():
    messagebox.showinfo(title = '알림', message = '업데이트 예정입니다.')


# -run------------------------------------------------------------ #
if __name__ == "__main__":
    mainWindow = tk.Tk()
    mainWindow.geometry("600x920+100-100")
    mainWindow.resizable(width = False, height = False)

    pusher()
    Timer()
    load_record()
    run()
    mainWindow.mainloop()
# ---------------------------------------------------------------- #
    
    
