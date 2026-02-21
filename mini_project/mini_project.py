#당뇨병 예측 데이터 분석
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#데이터 불러오기
data = pd.read_csv("/Users/goorm/desktop/goorm/medical/mini_project/diabetes.csv")

#데이터 정보 확인
print(data.head())
print("\n====columns====")
print(data.columns) #컬럼 이름 확인
print("\n====info====")
print(data.info()) #기본정보(결측치, dtype, 메모리)
print("\n====describe====")
print(data.describe()) #요약 통계(수치형 컬럼)

#결측치 찾아서 평균으로 채우기
#0->NaN으로 바꾸고 평균으로 채우기
#(0이 결측치처럼 잘못 들어간 걸로 보이는 컬럼 찾기)
zero_cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
#1) 0이 몇 개인지 확인
print("0 counts:")
print((data[zero_cols] == 0).sum())

#2) 0->NaN (결측으로 처리)
data[zero_cols] = data[zero_cols].replace(0, np.nan)

print("\nNaN counts after replacd:")
print(data[zero_cols].isnull().sum())

#3) 평균으로 채우기
data[zero_cols] = data[zero_cols].fillna(data[zero_cols].mean())

print("\nNaN counts after impute(mean):")
print(data[zero_cols].isnull().sum())

#그래프 그리기
#인슐린 수치가 높으면 정말 당뇨가 많을까?

#박스플롯
plt.figure(figsize=(6,5))
sns.boxplot(x="Outcome", y="Insulin", data=data)
plt.title("Insulin Distribution by Diabetes Outcome")
plt.xlabel("Outcome (0: No Diabetes, 1:Diabetes)")
plt.ylabel("Insulin Level")
plt.show()

#Barplot
plt.figure(figsize=(6,5))
sns.barplot(x="Outcome", y="Insulin", data=data)
plt.title("Average Insulin Level by Outcome")
plt.xlabel("Outcome (0: No Diabetes, 1: Diabetes)")
plt.ylabel("Mean Insulin Level")
plt.show()

#히스토그램
plt.figure(figsize=(8,5))
sns.histplot(data=data[data["Outcome"]==0],
             x="Insulin", kde=True, color="blue", label="No Diabetes", alpha=0.5)

sns.histplot(data=data[data["Outcome"]==1],
             x="Insulin", kde=True, color="red", label="Diabetes", alpha=0.5)

plt.legend()
plt.title("Insulin Distribution Comparison")
plt.show()