evens = 0
odds=0
while True:
    num = input("enter a no")
    if not num:
        break
    if not num.isnumeric():
        continue
    num = int(num)
    if num%2==0:
        evens+=num
    else:
        odds +=num

print(f"evens value added=> {evens}")
print(f"odd value added {odds}")     

    