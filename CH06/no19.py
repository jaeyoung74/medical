#산점도
#나이가 많을수록 혈압도 높을까?
#상관관게 확인
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/goorm/desktop/goorm/medical/ch06/heart_disease.csv")
print(data.head())
print(data.columns)

#원본 보존위해 복사
data_clean = data.copy()

#필요한 컬럼만 결측치 제거
x_col = "Age"
y_col = "Blood Pressure"

scatter_data = data_clean[[x_col, y_col]].dropna()
print(scatter_data.head())

#산점도 그리기
plt.figure(figsize=(8,6))
sns.scatterplot(
    data=scatter_data, 
    x=x_col, y=y_col, 
    alpha=0.08, #훨씬 더 투명하게
    s=10, #점 크기 줄이기
    linewidth=0, #테두리 없애서 덜 뭉개짐
)
plt.title("Age vs Blood Pressure")

plt.show()

