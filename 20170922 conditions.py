# Python Program - Example No.3

while True:
    print("Enter '0' for exit.")
    val = int(input("Guess a Number: "))
    if val == 0:
        break
    elif (val > 10 and val < 100):
        print("What a guess..!!\n")
    else:
        print("Opps..!!\n")