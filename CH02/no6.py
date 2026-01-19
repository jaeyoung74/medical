#자동 건강감진 판정기
#상황 : 우리 병원에서는 BMI 수치에 따라 비만 여부를 자동으로 판정해 주는 시스템이 필요합니다.
#미션 목표 : 아래 조건에 맞는 check_obesity라는 함수를 만들어 보세요.

def check_obesity(bmi):
    if bmi >= 30:
        return "비만"
    elif bmi >= 25:
        return "과체중"
    else:
        return "정상"
    
print(check_obesity(32)) 
print(check_obesity(24))   