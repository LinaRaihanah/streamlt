# Question 1

purchase = float(input("Enter purchase amount (RM): "))

if purchase < 100:
    points = 0
elif purchase <= 200:
    points = 5
elif purchase <= 300:
    points = 15
else:
    points = 30

print("Points awarded:", points)