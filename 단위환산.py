#### 단위 변환 ####

pound = int(input("파운드(1b)를 입력하세요 : "))
kg = pound*0.453592
print(pound, "파운드(lb)는", round(kg, 5), "킬로그램(kg) 입니다.")

kg = int(input("킬로그램(kg)을 입력하세요 : "))
pound = kg*2.204623
print(kg, "킬로그램(kg)은", round(pound, 5), "파운드(lb) 입니다.")
