#Exercise 1
num_list = []
for number in range(1, 11):
    number_cubed = number**3
    num_list.append(number_cubed)

for num in num_list:
    print(num)

#Exercise 2



  
for num in range(1, 542):

  if num>1:
    for new_num in range(2,num):
        if(num % new_num==0):
            break
    else:
        print(num)












#Exercise 3

print("enter ur age")
age = input()
new_age = int(age)


if new_age<18:
    print("kids")
elif new_age>=18:
    print("seniors")