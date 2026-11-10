num = int(input("enter your number: "))
if num > 0:
    print("ეს რიცხვი დადებითია")
elif num < 0:
    print("ეს რიცხვი უარყოფითია")
else:
    print("ეს რიცხვი ნულია")
    
    
    
num2 = int(input("enter your number: "))
if num2 % 2 == 0:
    print("ეს რიცხვი ლუწია")
else:
    print("ეს რიცხვი კენტია")
    
    
    
a = 15
b = 30 
if a > b:
    print("A დიდი რიცხვია")
elif b > a: 
    print("B დიდი რიცხვია")
else:
    print("ტოლია")
    
score = 75
if score >= 90:
    print("exsellent")  
elif score >= 89:
    print("good")
elif score >= 69:
    print("everage")
else:
    print("falled")
    
    
a = 12
b = 45
c = 27
if a > b and a > c:
    print("A is bigger")
elif b > a and b > c:
    print("B is bigger")
else:
    print("C is bigger")


price = 250 
if price > 300:
    print("ფასდაკლება 30%")
elif price > 200:
    print("ფასდაკლება 20%")
elif price > 100:
    print("ფასდაკლება 10%")
else:
    print("ფასდაკლება არ არის")
