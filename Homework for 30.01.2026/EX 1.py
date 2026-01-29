import json

with open("data.json") as file:
    lst = json.load(file)

count = 0
sum = 0

lst1 =[]

for i in lst:
    if i % 3 == 0:
        lst1.append(i)
        sum+=i
        count+=1

lst = lst1


with open("data1.json", "w") as file:
        json.dump(lst, file)

print(sum/count)


