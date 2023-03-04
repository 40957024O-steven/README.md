import pandas as pd #整理csv檔用
import matplotlib.pyplot as plt #繪製視覺化數據用


df = pd.read_csv("C:/Users/steven.LAPTOP-8A1BDJC6/OneDrive/桌面/程式課/README.md/text.csv",encoding='BIG5') #以GIB5的conding方式讀取csv檔
# print(df)
team = df[['類別','參加人數']] #選取出所需要的資料組
# print(team)

gb = team.groupby(['類別'])['參加人數'].sum().reset_index() #將資料以'類別'的方式分組並做'參加人數'的'加總'統計,並重新給予序列號
# print(gb)
x = gb['參加人數'] #將'參加人數'設為繪圖的數據
tick = gb['類別'] #將'類別'設為繪圖的組別名稱
# print(x)
# print(tick)



plt.rcParams['font.sans-serif'] = [u'MingLiu'] #設定字體為'細明體'
plt.rcParams['axes.unicode_minus'] = False #用來正常顯示正負號

#繪製圓餅圖
plt.pie(x, #數據
        labels = tick, #類別
        autopct="%1.2f%%", #數據顯示到小數點後第n位
        textprops = {"fontsize" : 10}, #字體大小
        pctdistance = 0.5, #數值位置
        shadow=True) #陰影

plt.legend() #設定圖例
plt.axis('equal') #使圓餅圖比例相等
plt.title('公務人員參訓人數',loc = 'left') #設定標題
plt.show() #顯示繪製的圖

