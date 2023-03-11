import pandas as pd

path = "C:/Users/steve/Desktop/學校/大三下/學習分析工具實務應用/README.md/text.csv"
df = pd.read_csv(path,encoding='BIG5')
# print(df)

day = df.groupby(['日期'])['參加人數'].sum().reset_index()
maxnb = 0
minnb = 99999999999999999
nb = 0
for i in day['參加人數']:
        nb += 1
countd = day.sum().values[1]
# 哪一天人數最多?
Q_1 = day.max()
# print(Q_1)

# 哪一天人數最少?
Q_2 = day.min()
# print(Q_2)

# 每天人數平均?
Q_3 = round(countd/nb,1)
# print(Q_3)


team = df.groupby(['類別'])['參加人數'].sum().reset_index()
# print(team)
nb = 0
for i in team['參加人數']:
        nb += 1
# 哪個類別人數最多?
Q_4 = team.max()
# print(Q_4)

# 哪個類別人數最少?
Q_5 = team.min()
# print(Q_5)

# 每類人數的平均?
countt =  team.sum().values[1]
Q_6 = round(countt/nb,1)
# print(Q_6)


time = df.groupby(['時間'])['參加人數'].sum().reset_index()
# print(time)
nb = 0
for i in time['時間']:
        nb += 1
# print(nb)
# 哪個時間人數最多?
Q_7 = time.max()
# print(Q_7)

# 哪個時間人數最少?
Q_8 = time.min()
# print(Q_8)

# 每個時間人數平均?
countti =  time.sum().values[1]
Q_9 = round(countti/nb,1)
# print(Q_6)

# 公務人員參訓總人數?
Q_10 = df['參加人數'].sum()
# print(Q_10)

print('\nQ1:哪一天人數最多??\nA1:\n'+ str(Q_1))
print('\nQ2:哪一天人數最少??\nA2:\n'+ str(Q_2))
print('\nQ3:每天人數平均??\nA3:'+ str(Q_3))
print('\nQ4:哪個類別人數最多??\nA4:\n'+ str(Q_4))
print('\nQ5:哪個類別人數最少??\nA5:\n'+ str(Q_5))
print('\nQ6:每類人數的平均??\nA6:'+ str(Q_6))
print('\nQ7:哪個時間人數最多??\nA7:\n'+ str(Q_7))
print('\nQ8:哪個時間人數最少??\nA8:\n'+ str(Q_8))
print('\nQ9:每個時間人數平均??\nA9:'+ str(Q_9))
print('\nQ10:公務人員參訓總人數??\nA10:'+ str(Q_10))
