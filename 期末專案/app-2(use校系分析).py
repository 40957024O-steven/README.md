import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext
import time 
from openpyxl import load_workbook
import os
# 功能：
# 按下按鈕後將對話框的內容顯示到輸出螢幕上
# 側邊有上下滾輪
# 機器人的話會顯示綠色

button_pressed = False
root = tk.Tk()

root.geometry("430x800")
root.title("升學機器人")

path = os.path.join(os.getcwd(),'期末專案/112校系分則.xlsx')
# print(path)
wb = load_workbook(path)
ws =  wb['112校系分則v1']
rowmax = ws.max_row
# print(rowmax)

def Gors(gors):
    if gors == "國立" or gors == '公立':
        for i in range(3,rowmax+1):
            schoolallname = ws.cell(i,3).value #學校名稱
            # print(schoolallname)
            gors = schoolallname[:2] #公私立
            # print(gors)
            if schoolallname != ws.cell(i-1,3).value:
                if gors == '國立':
                    text_area.insert(tk.END,schoolallname+"\n","tag_name")
        text_area.insert(tk.END,'\n\n請問要查詢的學校?'+"\n","tag_name")  

    elif gors == "私立":
        for i in range(3,rowmax+1):
            schoolallname = ws.cell(i,3).value #學校名稱
            # print(schoolallname)
            gors = schoolallname[:2] #公私立
            # print(gors)
            if schoolallname != ws.cell(i-1,3). value:      
                if gors != '國立':
                    text_area.insert(tk.END,schoolallname+"\n","tag_name")
        text_area.insert(tk.END,'\n\n請問要查詢的學校?'+"\n","tag_name")
 
def School(school):
    chack = 0  
    for i in range(3,rowmax+1):
        gp = ws.cell(i,4).value.replace(' ','')
        if school == str(ws.cell(i,3).value).replace(' ',''):
            text_area.insert(tk.END,gp+"\n","tag_name")
            serch[0] = school
            chack += 1
    if chack == 0:
        text_area.insert(tk.END,"查無此學校\n","tag_name")
    # print(serch)
    
serch = [[],[]] #所搜尋[[學校],[系所]]

def Conversation(conversation):
    if conversation == '國立' or conversation =='公立' or conversation =='私立':
        Gors(conversation)      
        # text_area.insert(tk.END,'公私立查詢'+"\n","tag_name")

    elif conversation[-2:] == '大學':
        School(conversation)
        # text_area.insert(tk.END,'學校名稱查詢'+"\n","tag_name")
    elif conversation[-1] == '系':
        text_area.insert(tk.END,'系所查詢'+"\n","tag_name")
    elif conversation == 'Del' or conversation =='del':
        text_area.insert(tk.END,'刪除所查詢資料'+"\n","tag_name")
    else:
        text_area.insert(tk.END,'輸入錯誤,請重輸入'+"\n","tag_name")
    print(conversation)
# 輸出螢幕
text_area = scrolledtext.ScrolledText(root, width=250, height=50)
text_area.tag_config("tag_name", foreground="green")
text_area.insert(tk.END,"機器人：\n請輸入以下指令進行互動\n您所要查詢的大學是國立(公立)OR私立?\n","tag_name")

text_area.pack()


def handle_button_press():
    # 获取对话框的文本
    t = enterwindow.get("1.0","end").replace('\n','').replace(' ','')
    # print(t)
    # 清空对话框的文本
    enterwindow.delete("1.0", tk.END)
    # 在输出框中添加文本
    text_area.insert(tk.END, "\n您：\n{}\n\n".format(t))
    # print(t)
    text_area.insert(tk.END,"機器人：\n","tag_name")   
    # print(t)     
    Conversation(t)



# 對話框
enterwindow = tk.Text(root, width=50, height=10)
enterwindow.place(x=5,y=662) 

# 輸入按鈕
bt = tk.Button(root, text='輸入',width=8,height=4,command=handle_button_press)
bt.place(x=362,y=692) 



root.mainloop()
