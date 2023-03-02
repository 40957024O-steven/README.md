import pandas as pd

df = pd.read_csv("C:/Users/steven.LAPTOP-8A1BDJC6/OneDrive/桌面/程式課/README.md/text.csv",encoding='BIG5')
print(df.describe)
df[['日期','參加人數']]