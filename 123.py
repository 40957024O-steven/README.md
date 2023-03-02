import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("C:/Users/steve/Desktop/學校/大三下/學習分析工具實務應用/README.md/text.csv",encoding='BIG5')
# print(df)
team = df[['類別','參加人數']]
# print(team)

gb = team.groupby(['類別'])['參加人數'].sum().reset_index()
# print(gb)
x = gb['參加人數']
tick = gb['類別']
print(x)
print(tick)



plt.rcParams['font.sans-serif'] = [u'MingLiu'] 
plt.rcParams['axes.unicode_minus'] = False 

plt.pie(x,labels = tick,autopct="%1.2f%%",textprops = {"fontsize" : 10},pctdistance = 0.5,shadow=True)
plt.legend()
plt.axis('equal') #使圓餅圖比例相等(雖然我看不出來哪裡有差)
plt.title('公務人員參訓人數',loc= 'left')
plt.show()