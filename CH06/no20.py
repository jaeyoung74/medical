#히스토그램
#우리 병원 환자들은 주로 몇 살일까?
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/goorm/desktop/goorm/medical/ch06/heart_disease.csv")
print(data.head())

#원본 보존
data_clean = data.copy()

#나이만 뽑고 결측치 제거
age_col = "Age"
age_data = data_clean[[age_col]].dropna()

#히스토그램 그리기
plt.figure(figsize=(8,6))
sns.histplot(
    data=age_data,
    x=age_col,
    bins=20,
    kde=True
)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()