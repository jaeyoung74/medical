#Seaborn 라이브러리
#python의 데이터 시각화 라이브러리
#matplotlib를 기반으로 작동
import seaborn as sns
import matplotlib.pyplot as plt

#데이터셋 로드
tips = sns.load_dataset("tips")

#히스토그램
sns.histplot(data=tips, x="total_bill", kde=True)
plt.show()

#산점도
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="sex")
plt.show()

#박스플롯
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")
plt.show()
