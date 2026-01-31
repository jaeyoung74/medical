#결측치 처리
#비어있는 혈압 데이터를 평균값으로 채우거나,
#데이터가 없는 행을 지우기

import pandas as pd

data = {
    "이름":["a", "b", "c", "d", "e", "f"],
    "나이":[20, 30, 23, 45, 60, 33], 
    "혈압":[120, None, 130, None, 78, 100],
}

df = pd.DataFrame(data)
print(df.isnull())

#비어있는 혈압 데이터를 평균값으로 채우기
mean = df["혈압"].mean()
print(mean)

df["혈압"] = df["혈압"].fillna(mean)
print(df)

#데이터가 없는 행을 지우기
data1 = {
    "이름":["a", "b", "c", "d", "e", "f"],
    "나이":[20, 30, 23, 45, 60, 33], 
    "혈압":[120, None, 130, None, 78, 100],
    "키":[160, 179, 155, 167, 180, 145],
    "몸무게":[67, 70, 50, 55, 85, 40]
}
df1 = pd.DataFrame(data1)

print(df1.dropna())