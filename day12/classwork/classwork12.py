num1 = int(input("enter first number: "))
num2 = int(input("enter secund number: "))

if num1 > num2:
    print("higest number", num1)
elif num2 > num1:
    print("higest number", num2)
else:
    print("equal number")
    
score = 85
if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("c")
elif score >= 60 and score <= 69:
    print("D")
else:
    print("filed")
    
    
num = 30
if num % 3 == 0:
    print("რიცხვი იყოფა 3-ზე")
    
    
    
if num % 5 == 0:
    print("რიცხვი იყოფა 5 ზე")
    
    
    
if num % 3 == 0 and num % 5 == 0:
    print("რიცხვი იყოფა ორივეზე")
    
    
price = 150
if price > 150:
    print("ფასდაკლება 20%")
elif price > 100:
    print("ფასდაკლება 10%")
else:
    print("სხვა შემთხვევაში ფასდაკლება არაა")

