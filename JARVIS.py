import datetime
import pyautogui
import pyperclip
import googletrans
import subprocess
import webbrowser
import tkinter
import threading
import time
import re

"""
    # 今日の天気
    elif ("今日" in x) and ("天気" in x):
        print(f"\nF.R.I.D.A.Y.:天気予報を表示します。")
        webbrowser.open("https://weathernews.jp/onebox/34.770513/135.4953036/")

    elif x == "EV3":
        print(f"\nF.R.I.D.A.Y.:EV3を起動します。")
        subprocess.Popen("C:/Program Files (x86)/LEGO Software/LEGO MINDSTORMS Edu EV3/MindstormsEV3.exe")

    elif x == "SPIKE":
        print(f"\nF.R.I.D.A.Y.:SPIKEを起動します。")
        subprocess.Popen("C:/Program Files/SPIKE/SPIKE-win-2.0.7.54086-allContent.exe")

    elif x == "音楽":
        print(f"\nF.R.I.D.A.Y.:iTunesを起動します。")
        subprocess.Popen("C:/Program Files/iTunes/iTunes.exe")

    elif x == "映画":
        print(f"\nF.R.I.D.A.Y.:Disney+を表示します。")
        webbrowser.open("https://www.disneyplus.com/ja-jp/home")

    elif x == "予定":
        print(f"\nF.R.I.D.A.Y.:カレンダーを起動します。")
        webbrowser.open("https://calendar.google.com/calendar/u/0/r")

    elif x == "メール":
        print(f"\nF.R.I.D.A.Y.:Gmailを起動します。")
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
"""

root = tkinter.Tk()
root.title("J.A.R.V.I.S.")
root.configure(bg="black")
root.geometry("400x250")

dt = datetime.datetime.now()
if 4 <= dt.hour < 12:
    g = "おはようございます"
elif 12 <= dt.hour < 19:
    g = "こんにちは"
else:
    g = "こんばんは"

jarvis = tkinter.Label(text=f"{g}、朋樹様。\n\nご用件は何でしょうか？", font=("MS Gothic", 9, "bold"), fg="white", bg="black")

sv = tkinter.StringVar()
e = tkinter.Entry(width=40, textvariable=sv)

def f():
    if re.search(sv.get(), "検索ブラウザ"):
        jarvis["text"] = "ブラウザを起動します。"
        webbrowser.open("https://www.google.com/?hl=ja")
        e.delete(0, tkinter.END)

    elif re.search(sv.get(), ".+を和訳"):
        tr = googletrans.Translator()
        text = sv.get()
        result = tr.translate(text, src="en", dest="ja").text
        jarvis["text"] = result
        e.delete(0, tkinter.END)

    elif re.search(sv.get(), ".+を英訳"):
        tr = googletrans.Translator()
        text = sv.get()
        result = tr.translate(text, src="ja", dest="en").text
        jarvis["text"] = result
        e.delete(0, tkinter.END)

    else:
        jarvis["text"] = "登録されていないコマンドです。"
        e.delete(0, tkinter.END)

b = tkinter.Button(text="送信", width=5, command=f)

wd = ["月", "火", "水", "木", "金", "土", "日"]
clock = tkinter.Label(text=f"                    {dt.year}/{dt.month}/{dt.day}({wd[dt.weekday()]}) {dt.hour:02}:{dt.minute:02}:{dt.second:02}", font=("MS Gothic", 9, "bold"), fg="white", bg="black")
def dt_func():
    while True:
        dt = datetime.datetime.now()
        clock["text"] = f"                    {dt.year}/{dt.month}/{dt.day}({wd[dt.weekday()]}) {dt.hour:02}:{dt.minute:02}:{dt.second:02}"
        time.sleep(1)
thread = threading.Thread(target=dt_func, daemon=True)
thread.start()

jarvis.pack()
clock.pack(side=tkinter.BOTTOM)
b.pack(side=tkinter.BOTTOM, pady=10)
e.pack(side=tkinter.BOTTOM)

root.mainloop()