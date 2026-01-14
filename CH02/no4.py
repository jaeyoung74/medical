#함수
#나만의 의료 프로토콜 만들어보기

#예제. 비만도(BMI)계산기 만들기
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi

result1 = calculate_bmi(70, 175)
result2 = calculate_bmi(90, 180)

print(f"환자 1의 BMI: {result1:.1f}")
print(f"환자 2의 BMI: {result2:.1f}")

#실습1
#기초대사량(BMR) 계산기 만들기
#gender : 여자=1, 남자=2
def calculate_bmr(gender, age, height, weight):
    bmr = 0
    if gender == 1:
        bmr = 10*weight + 6.25*height - 5*age - 161
    elif gender == 2:
        bmr = 10*weight + 6.25*height - 5*age + 5
    else:
        return "없는 성별입니다! 다시 입력해주세요!!"
    return bmr

result1 = calculate_bmr(1, 20, 160, 50)
result2 = calculate_bmr(2, 30, 180, 70)
result3 = calculate_bmr(3, 40, 155, 55)

print(f"환자 1의 bmr: {result1:.1f}")
print(f"환자 2의 bmr: {result2:.1f}")
print(f"환자 3의 bmr: {result3}")

#실습2
#혈압 분류기
#수축기(SBP), 이완기(DBP)
def calculate_bp(sbp, dbp):
    if sbp < 120 and dbp < 80:
        return "정상 혈압"
    elif 120 <= sbp <= 129 or dbp < 80:
        return "고혈압 전단계"
    elif 130 <= sbp <= 139 or 80 <= dbp <= 89:
        return "1기 고혈압"
    else:
        return "2기 고혈압"

result1 = calculate_bp(80, 100)
result2 = calculate_bp(80, 70)
result3 = calculate_bp(130, 70)

print(f"환자 1은: {result1}입니다.")
print(f"환자 2은: {result2}입니다.")
print(f"환자 3은: {result3}입니다.")