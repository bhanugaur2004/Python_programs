num = int(input("Enter a number: "))
num = num + 1
while True:
    temp = num
    digits = 0
    while temp>0:
        digits += 1
        temp //= 10
        # print(temp)
    temp = num
    total = 0
    while temp>0:
        digit = temp%10
        total += digit ** digits
        temp //= 10
    if total == num:
        print("Next Armstrong number: ", num)
        break
    num +=1