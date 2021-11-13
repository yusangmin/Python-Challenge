print("=*50")
print("점수기준\n100점에서 90점 이상   A\n90점 미만 80점 이상   B\n80점 미만70점 이상    C \n70점 미만 60점 이상   D\n60점 미만             F")
print("=*50")
score = int(input("점수를 입력하십시오: "))

if score >= 90 or score == 100:
  print("A학점 입니다.")
elif score < 90 and score >= 80: 
  print("B학점 입니다.") 
elif score < 80 and score >= 70:
   print("C학점 입니다.")      
elif score < 70 and score >= 60:
  print("D학점 입니다.")
else :
  print("F학점 입니다.")