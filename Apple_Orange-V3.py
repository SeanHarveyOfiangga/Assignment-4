# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

def Apple_Orange (Apple, Orange):
    PriceApple = 20
    PriceOrange = 25
    Amount = (Apple*PriceApple) + (Orange*PriceOrange)
    print (f"The total amount is {Amount}.")

Apple = int(input("How many apples do you want to buy? : "))
Orange = int(input("How many oranges do you want to buy? : "))

Apple_Orange (Apple, Orange)