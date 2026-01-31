#고위험군 자동 필터링
import pandas as pd

data = {
    "이름": ["김철수", "이영희", "박민수", "최지혜", "정수진"],
    "나이": [45, 32, 58, 29, 62],
    "성별": ["남", "여", "남", "여", "여"],
    "혈당": [95, 88, 140, 79, 150]
}

df = pd.DataFrame(data)

high_glucose = df[df['혈당'] >= 120]
print(high_glucose)