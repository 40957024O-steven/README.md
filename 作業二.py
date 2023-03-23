import matplotlib.pylab as plt
import pandas as pd
import numpy as np 

df = pd.read_csv("C:/Users/steven.LAPTOP-8A1BDJC6/OneDrive/桌面/程式課/README.md/text.csv",encoding='BIG5')
# print(df)

inf = df[['類別','參加人數']]
# print(inf)

s = inf.groupby(['類別'])['參加人數'].sum().reset_index()['參加人數']
print(s) #總人數

a = inf.groupby(['類別'])['參加人數'].max().reset_index()['參加人數']
print(a) #最大值

i = inf.groupby(['類別'])['參加人數'].min().reset_index()['參加人數']
print(i) #最小值

ti = inf.groupby(['類別'])['參加人數'].min().reset_index()['類別']
print(ti)

x = np.arange(len(ti))
print(x)
plt.rcParams['font.sans-serif'] = [u'MingLiu'] #設定字體為'細明體'
plt.rcParams['axes.unicode_minus'] = False #用來正常顯示正負號

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()


curve1 = ax1.bar(x,s,label="總人數",width=0.2,color = 'g')
curve2, = ax2.plot(x, a, label="最大值", color='b')
curve3, = ax2.plot(x, i, label="最小值", color='r')



curves = [curve1, curve2,curve3]


ax1.legend(curves, [curve.get_label() for curve in curves])

plt.xticks(x,ti)
ax1.set_ylabel('總人數')
ax2.set_ylabel('最大值&最小值人數',rotation = 270,labelpad=10)


plt.title('依類別統計人數')
plt.show()


#問題
# Q1: 不同類別人數分布為何?
# Q2: 不同類別人數最大值分布為何?
# Q3: 不同類別人數最小值分布為何?




