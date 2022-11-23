#Q1
number=[12, 75, 150, 180, 145, 525, 50]
for item in number:
    if item%5==0 and item>150:
        continue
    elif item%5==0 and item>500:
        break
    else:
        if item%5==0:
            print(number[number.index(item)])
print("----------")
#Q2
for i in range(5):
  print(i)
  if i<4:
      continue
  else:print("Done!")
  print("----------")

#Q3
num = 76542
reversed = 0

while num != 0:
    digit = num % 10
    reversed = reversed * 10 + digit
    num //= 10

print(str(reversed))
print("----------")

#Q4
res={}
keys=['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
for key in keys:
    for value in values:
        res[key] = value
        values.remove(value)
        break
print(str(res))
print("----------")

#Q5

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
rev_dict={"name","salary"}
for key in rev_dict:
    sample_dict.pop(key)
print(sample_dict)
print("----------")
#Q6
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
for key in sample_list:
    sample_set.add(key)
print(sample_set)
print("----------")
#Q7
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
return_v=set1.intersection(set2)

print(return_v)
print("----------")
















