import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext

# 功能：
# 按下按鈕後將對話框的內容顯示到輸出螢幕上
# 側邊有上下滾輪
# 機器人的話會顯示紅色

button_pressed = False
root = tk.Tk()

root.geometry("430x800")
root.title("升學機器人")

# 輸出螢幕
text_area = scrolledtext.ScrolledText(root, width=250, height=50)
text_area.tag_config("tag_name", foreground="red")
text_area.insert(tk.END,"機器人：\n請輸入以下指令進行互動\n","tag_name")
text_area.pack()

def handle_button_press():
    # 获取对话框的文本
    t = enterwindow.get("1.0","end")
    # 清空对话框的文本
    enterwindow.delete("1.0", tk.END)
    # 在输出框中添加文本
    text_area.insert(tk.END, "\nYou said：\n{}".format(t))

# 對話框
enterwindow = tk.Text(root, width=50, height=10)
enterwindow.place(x=5,y=662) 

# 輸入按鈕
bt = tk.Button(root, text='輸入',width=8,height=4,command=handle_button_press)
bt.place(x=362,y=692) 


root.mainloop()
