m=int(input("math: "))
e=int(input("eng: "))
p=int(input("pys: "))

total_marks="m+e+p"
avarage ="total_marks/3"

percentage = "(total_marks/300)*100"
grade=""
if percentage > 90 :
    grade= "A"
elif percentage > 80 and per <= 90 :
    grade= "B"
elif percentage > 70 and per <= 80 :
    grade= "C"   
else:
    grade= "f"
print(f"total marks={total_marks} \navarage={avarage}\npercentage={per}\ngrade={grade}")        