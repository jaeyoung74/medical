#정렬하기
#혈당 높은 순서대로 줄 세우기
import pandas as pd

data = {
    "이름" : ["a", "b", "c", "d", "e"],
    "나이": [22, 30, 34, 29, 35],
    "성별": ["여", "남", "야", "남", "여"],
    "혈당" : [120, 135, 137, 110, 145]
}

df = pd.DataFrame(data)

#혈당 높은 순
result = df.sort_values(by="혈당", ascending=False)
print(result)