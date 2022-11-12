### 편의점 매출액 계산 ###

total = int(0)

#구매
coffee = int(input("캔 커피 구매 개수 : ")) #커피 구매
total -= 500*coffee
kimbap = int(input("삼각김밥 구매 개수 : ")) #삼각김밥 구매
total -= 900*kimbap
banana = int(input("바나나 우유 구매 개수 : ")) #바나나 우유 구매
total -= 800*banana
lock = int(input("도시락 구매 개수 : ")) #도시락 구매
total -= 3500*lock
coke = int(input("콜라 구매 개수 : ")) #콜라 구매
total -= 700*coke
shrimp = int(input("새우깡 구매 개수 : ")) #새우깡 구매
total -= 1000*shrimp

#판매
coffee2 = int(input("캔 커피 판매 개수 : ")) # 커피 판매
total += 1800*coffee2
kimbap2 = int(input("삼각김밥 핀매 개수 : ")) # 삼각김밥 판매
total += 1400*kimbap2
banana2 = int(input("바나나 우유  판매 개수 : ")) #바나나 우유 판매
total += 1800*banana2
lock2 = int(input("도시락 판매 개수 : ")) #도시락 판매
total += 4000*lock2
coke2 = int(input("콜라 판매 개수 : ")) #콜라 판매
total += 1500*coke2
shrimp2 = int(input("새우깡 판매 개수 : ")) #새우깡 판매
total += 2000*shrimp2

print("오늘 총 매출액은", total, "원 입니다.")
