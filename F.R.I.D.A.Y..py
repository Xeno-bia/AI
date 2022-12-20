import datetime
import pyautogui
import pyperclip
import googletrans
import subprocess
import webbrowser

dt = datetime.datetime.now()
if 4 <= dt.hour < 12:
    print("F.R.I.D.A.Y.:おはようございます。")
elif 12 <= dt.hour < 19:
    print("F.R.I.D.A.Y.:こんにちは。")
else:
    print("F.R.I.D.A.Y.:こんばんは。")

while True:
    print("\nF.R.I.D.A.Y.:ご用件は何でしょうか？")
    x = input("\n      あなた:")

    if ("今日" in x) and (("何日" in x) or ("日付" in x)):
        wd = ["月", "火", "水", "木", "金", "土", "日"]
        print(f"\nF.R.I.D.A.Y.:今日は、{dt.year}年{dt.month}月{dt.day}日{wd[dt.weekday()]}曜日です。")

    elif (("今" in x) or ("現在" in x)) and (("何時" in x) or ("時刻" in x)):
        print(f"\nF.R.I.D.A.Y.:現在の時刻は、{dt.hour}時{dt.minute}分{dt.second}秒です。")

"""
    elif x == "VS Code":
        print(f"\nF.R.I.D.A.Y.:VS Codeを起動します。")
        subprocess.Popen()

    elif x == "EV3":
        print(f"\nF.R.I.D.A.Y.:EV3を起動します。")
        subprocess.Popen("C:/Program Files (x86)/LEGO Software/LEGO MINDSTORMS Edu EV3/MindstormsEV3.exe")

    elif x == "SPIKE":
        print(f"\nF.R.I.D.A.Y.:SPIKEを起動します。")
        subprocess.Popen("C:/Program Files/SPIKE/SPIKE-win-2.0.7.54086-allContent.exe")

    elif x == "音楽":
        print(f"\nF.R.I.D.A.Y.:iTunesを起動します。")
        subprocess.Popen("C:/Program Files/iTunes/iTunes.exe")

    elif x == "検索":
        print(f"\nF.R.I.D.A.Y.:ブラウザを起動します。")
        webbrowser.open("https://www.google.com/?hl=ja")

    elif x == "予定":
        print(f"\nF.R.I.D.A.Y.:カレンダーを起動します。")
        webbrowser.open("https://calendar.google.com/calendar/u/0/r")

    elif x == "メール":
        print(f"\nF.R.I.D.A.Y.:Gmailを起動します。")
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

    elif x == "和訳":
        print(f"\nF.R.I.D.A.Y.:何を和訳しますか？")
        text = input("\n      あなた:")
        tr = googletrans.Translator()
        result = tr.translate(text, src="en", dest="ja").text
        print(f"\nF.R.I.D.A.Y.:{result}")

    elif x == "英訳":
        print(f"\nF.R.I.D.A.Y.:何を英訳しますか？")
        text = input("\n      あなた:")
        tr = googletrans.Translator()
        result = tr.translate(text, src="ja", dest="en").text
        print(f"\nF.R.I.D.A.Y.:{result}")

    elif x == "bye":
        print("\nF.R.I.D.A.Y.:さようなら。")
        break

    else:
        print("\nF.R.I.D.A.Y.:よく分かりません。")
"""

"""
おはよう
    おはようございます。

こんにちは
    こんにちは。

こんばんは
    こんばんは。

いってきます
    いってらっしゃいませ。

ただいま
    おかえりなさいませ。

さようなら or バイバイ
    さようなら。

お疲れ
    お疲れ様です。

おやすみ
    おやすみなさい。

よろしく
    よろしくお願いします。

ありがとう
    とんでもないです。

ごめん
    とんでもないです。

今は何年？
    今年は、？年です。

今日は何曜日？
    今日は、？曜日です。

今は何時？
    現在は、？時？分？秒です。

今日の予定は？
    Googleカレンダーを起動します。 or ？時？分から？があります。

？にメール
    Gmailを起動します。 or 件名 本文

音楽が聴きたい
    iTunesを起動します。

映画が見たい
    Disney+を起動します。
"""