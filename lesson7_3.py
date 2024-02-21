import pyinputplus as pyip
import random
min=1
max=100
count = 0
random_number = random.randint(min,max)

while True:
    keyin = pyip.inputInt(f"猜數字範圍{min}~{max}:")
    count += 1
    print(keyin)
    if keyin == random_number:
        print(f"賓果!答對了,答案是:{random_number}")
        print(f"您猜了{count}次")
        break

    elif keyin > random_number:
        print(f"再小一點")
        max = keyin - 1
    elif keyin < random_number:
        print(f"再大一點")
        min = keyin + 1 
        print(f"您猜了{count}次")
        print("============================")

print("===========猜數字遊戲============")