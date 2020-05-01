tempss = [9.1,8,8,8.7,90,87] 
student_grades= {"Chandan":100,"Neha":200,"Vikash":500}
mysum = sum(tempss)/len(tempss)
print(student_grades.values())
print(student_grades.keys())
print(student_grades)
print(tempss)
tempss.append(90)
print(tempss)
print(tempss.index(9.1))

print(tempss.index(9.1,0))

tempss.remove(8.7)
print(tempss[1])
print(tempss[1:3])
print(tempss[:2])