import time
x = int(input("Please Enter Number:"))

while True:
    print(x)
    x-= 1
    time.sleep(1)
    if x == -1: 
        print("Finished")
        break
    elif x <0:
        print("Invalid Number")
        break