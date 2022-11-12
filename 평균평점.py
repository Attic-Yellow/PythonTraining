### 기말 학점 평균 구하기 ###

total = 0

#교과명에 학점을 저장
python = 3
mobile = 2
exal = 1

#학점별 점수
Aplus = 4.5
Azero = 4.0
Bplus = 3.5

#학점 총합
total = python * Bplus + mobile * Azero + exal * Aplus
print("학점 총합", total)
#학점 평균
avg = total / (python + mobile + exal)
print("평균 학점", round(avg, 2))
