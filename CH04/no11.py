#조건 필터링
#30대 여성이면서 혈압이 130 이상인 사람 뽑기
import pandas as pd

data = {
    "이름" : ["a", "b", "c", "d", "e"],
    "나이": [22, 30, 34, 29, 35],
    "성별": ["여", "남", "여", "남", "여"],
    "혈당" : [120, 135, 137, 110, 145]
}

df = pd.DataFrame(data)
print(df)

result = df[df["나이"].between(30,39) & (df["성별"]=="여") & (df["혈당"]>=130)]
print(result)

