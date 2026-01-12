#상황판단 만들기

#1
#의사의 진단 논리를 만들기 = 만약~라면 A를 하고, 아니면 B를 해라
tmp = 37.5
if tmp >= 38.0:
    print("열이 좀 높네요")
elif tmp >= 37.0:
    print("미열이 나네요")
else:
    print("열이 없어요")
print()

#2
#간호사의 회진 = 환자의 정보를 반복해서 확인한다
tmp = [36.0, 37.5, 38.0]
for i in tmp:
    if i >= 38.0:
        print("열이 좀 높네요")
    elif i >= 37.0:
        print("미열이 나네요")
    else:
        print("열이 없네요")