# wap a program to add 10 no in a list by users
num =[]   # blank list
for i in range(10):
    data = input("enter a number")
    if data.isnumeric():
        num.append(int(data))

print("your data =>",num)
