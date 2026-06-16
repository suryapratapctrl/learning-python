#what i did
secret_num = 7
attempts=1
num = int(input("Guess the number: "))

while secret_num != num:
    attempts+=1
    if secret_num > num:
        print("Guess higher")
    else:
        print("Guess lower")

    num = int(input("Guess again: "))
if secret_num==num:
    print("You guessed right!")

print(f"number of attemps {attempts}")
