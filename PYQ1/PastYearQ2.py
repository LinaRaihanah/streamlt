# Question 2

# Function 1: Calculate total price
def calculate_price(kid, adult):
    total_kid = kid * 50
    total_adult = adult * 100
    total = total_kid + total_adult

    return total_kid, total_adult, total


# Function 2: Calculate payment after discount
def calculate_payment(total):
    if total >= 300:
        discount = total * 0.10
    elif total > 200:
        discount = total * 0.05
    else:
        discount = 0

    payment = total - discount

    return payment


# Main program
kid = int(input("Enter number of kids: "))
adult = int(input("Enter number of adults: "))

total_kid, total_adult, total = calculate_price(kid, adult)

payment = calculate_payment(total)

print("Total price for kids: RM", total_kid)
print("Total price for adults: RM", total_adult)
print("Overall total price: RM", total)
print("Overall total payment after discount: RM", payment)


# Save output into DailySales.txt
file = open("DailySales.txt", "w")

file.write("D'Warung Cafe Daily Sales\n")
file.write("--------------------------\n")
file.write("Total price for kids: RM " + str(total_kid) + "\n")
file.write("Total price for adults: RM " + str(total_adult) + "\n")
file.write("Overall total price: RM " + str(total) + "\n")
file.write("Overall total payment after discount: RM " + str(payment) + "\n")

file.close()