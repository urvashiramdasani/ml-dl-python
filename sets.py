# Enter your code here. Read input from STDIN. Print output to STDOUT
a = {}
res = True
#while(i = int(input)):
 #   a.add(i)
n = int(input)
for i in (1,n+1):
    temp = {}
    while(num = int(input)):
        temp.add(num)
    res = a.issuperset(temp)
    if res==False:
        break
print(res)
