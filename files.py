import sys

f1 = open(sys.argv[1],"r")
f2 = open(sys.argv[2],"r")

wages = []
hours = []
id1 = []
name = []

for line in f1:
  word = line.strip().split(",") #strip() is used to remove \n
  hours.append(word[2])
  name.append(word[1])
  id1.append(word[0])
#print(hours)

for line in f2:
  word = line.strip().split(",")
  wages.append(word[1])
#print(wages)

new_wages = []
new_hours = []
salary = []
new_salary = []

for i in wages:
  new_wages.append(int(i))
for i in hours:
  new_hours.append(int(i))
for i in range(0,3):
  salary.append(new_wages[i]*new_hours[i])
#print(salary)

f3 = open("file3.txt","w")
for i in range(0,3):
  new_salary.append(str(salary[i]))
#print(new_salary)
for i in range(0,3) :
  f3.write(new_salary[i]+"\n")