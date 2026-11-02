i = 0

while i <= 20:
    print(i)
    i += 1
    
    
i = 20

while i >= 0:
    print(i)
    i -= 1


i = 0

while i <= 50:
    print(i)
    i += 2

i = 50

while i >= 0:
    print(i)
    i -= 3


password = "zura"

ask = input("enter your password: ")
while ask != password:
    user = input("correct password: ")
    print("enter new password")