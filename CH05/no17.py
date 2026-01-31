#BMI 자동 계산기
#키와 몸무게 데이터가 있는 표를 만들고
#코드로 계산해서 맨 오른쪽 열에 BMI 수치를 자동으로 채워 넣으세요
#결측치가 있다면 0으로 채우세요

import pandas as pd

data = {
    "cm": [150, 160, None, 188, 155],
    "kg": [60, 55, 68, 79, None]
}

df = pd.DataFrame(data)

df = df.fillna(0)
    
df["BMI"] = 0.0
#둘 다 0 이 아닌 행만 True
mask = (df["cm"] != 0) & (df["kg"] != 0)

df.loc[mask, "BMI"] = df.loc[mask, "kg"] / ((df.loc[mask, "cm"] / 100) ** 2)
print(df)