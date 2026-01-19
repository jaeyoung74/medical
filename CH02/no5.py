#라이브러리
#남이 만든 의료기기 가져와보자

#math: 수학 계산 도구
import math

#예제
#maht.pi : 원주율(3.1415292...)
area = 5 * 5 * math.pi
print(f"반지름 5인 세포의 면적: {area:.2f}")

#실습
#math.sqrt() : 제곱근
a = math.sqrt(4)
print(a)

#math.pow() : 거듭제곱
b = math.pow(2,3) #2의 3거듭제곱(2^3)
print(b)

#math.e : 자연상수
print(math.e)

#math.log() : 로그값
c = math.log(2.718281828459045)
print(c)

#math.log10() : 밑을 10으로 하는 로그값
d = math.log10(10)
print(d)

#math.degrees(라디안값) : 라디안 -> 60분법
e = math.degrees(math.pi)
print(e)
#math.radians(60분법값) : 60분법 -> 라디안
f = math.radians(180)
print(f)

#math.삼각함수이름(라디안값)
g = math.sin(math.pi / 2)
print(g)
h = math.cos(math.pi / 2)
print(h)
