#박스플롯
#남성과 여성의 당뇨 수치 차이 비교하기
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/goorm/desktop/goorm/medical/ch06/diabetes.csv")

#원본 보존
data_clean = data.copy()

#필요한 컬럼
x_col = "gender"
y_col = "glyhb"

#결측치 제거
box_data = data_clean[[x_col, y_col]].dropna()

#박스플롯
plt.figure(figsize=(8,6))
sns.boxplot(
    data=box_data, 
    x=x_col, y=y_col
)
#점도 같이
sns.stripplot(
    data=box_data,
    x=x_col, y=y_col,
    alpha=0.35,
    jitter=0.25
)

#당뇨 기준선 표시 (HbA1c 6.5)
plt.axhline(6.5, linestyle="--")
plt.title("HbA1c (glyhb) by Gender")
plt.xlabel("Gender")
plt.ylabel("HbA1c (glyhb)")
plt.show()