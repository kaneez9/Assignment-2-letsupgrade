#Assignment day 2
# Question 1
list=[]
for i in range (10):
    if i%2==0:
        list.append(i)
print(list)
#Question 3 solution

n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)
#question 4
pos = {"x":0,"y":0}
num = int(input())

for _ in range (num):
    command =  input().split(" ")      
    if command[0] == "UP":             
        pos["y"] += int(command[1])    
    if command[0] == "DOWN":
        pos["y"] -= int(command[1])
    if command[0] == "LEFT":
        pos["x"] -= int(command[1])
    if command[0] == "RIGHT":
        pos["x"] += int(command[1])

print(int(round((pos["x"]**2 + pos["y"]**2)**0.5))) 
