#파생변수 만들기
#키와 몸무게 컬럼을 이용해 BMI 컬럼을 새로 만들어 표에 붙이기

import pandas as pd

data = {
    "이름":["a", "b", "c", "d", "e"],
    "키":[130, 150, 187, 165, 155],
    "몸무게":[27, 45, 78, 77, 60]
}

df = pd.DataFrame(data)
print(df)