#타이타닉
#나이에 따른 생존율 그래프로 그리기
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/goorm/desktop/goorm/medical/ch06/train_and_test2.csv")

#원본 보존
df_clean = df.copy()

#필요한 컬럼 결측치 제거
x_col = "Age"
y_col = "2urvived"
plot_df = df[[x_col, y_col]].dropna()

#나이구간
bins=[0,10,20,30,40,50,60,70,80,100]
labels=["0-9","10-19","20-29","30-39","40-49","50-59","60-69","70-79","80+"]
plot_df["AgeGroup"] = pd.cut(plot_df[x_col], bins=bins, labels=labels, right=False)

plt.figure(figsize=(10,6))
sns.barplot(
    data=plot_df,
    x="AgeGroup",
    y=y_col
)
plt.title("Survival Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Survival Rate")
plt.show()
